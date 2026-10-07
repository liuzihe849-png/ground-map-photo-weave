import Foundation
import AppKit
import MapKit
// Genuine Apple map capture. Query must match a returned landmark name exactly.
guard CommandLine.arguments.count == 5,
      let lat = Double(CommandLine.arguments[2]), let lon = Double(CommandLine.arguments[3]) else {
    fputs("Usage: swift capture-mapkit.swift 'exact landmark name' hint-lat hint-lon /absolute/map.png\n", stderr); exit(1)
}
let query = CommandLine.arguments[1], output = CommandLine.arguments[4]
let request = MKLocalSearch.Request()
request.naturalLanguageQuery = query
request.region = MKCoordinateRegion(center: CLLocationCoordinate2D(latitude:lat,longitude:lon),span:MKCoordinateSpan(latitudeDelta:0.1,longitudeDelta:0.1))
var done = false, success = false
var snapshotter: MKMapSnapshotter?
MKLocalSearch(request:request).start { response,error in
    guard let items = response?.mapItems else { fputs("Search failed: \(error?.localizedDescription ?? "unknown")\n",stderr);done=true;return }
    let matches = items.filter { $0.name == query }
    guard matches.count == 1, let item = matches.first else {
        for item in items { print("Candidate: \(item.name ?? "unnamed")") }
        fputs("Need one verified exact landmark match; refine the query.\n",stderr);done=true;return
    }
    let coordinate = item.placemark.coordinate
    let options = MKMapSnapshotter.Options()
    options.region = MKCoordinateRegion(center:coordinate,span:MKCoordinateSpan(latitudeDelta:0.0055,longitudeDelta:0.0100))
    options.size = NSSize(width:1200,height:760)
    options.mapType = .standard; options.showsBuildings = true
    options.appearance = NSAppearance(named:.aqua)
    snapshotter = MKMapSnapshotter(options:options)
    snapshotter!.start(with:DispatchQueue.main) { snapshot,error in
        defer { done = true }
        guard let snapshot = snapshot, let tiff = snapshot.image.tiffRepresentation,
              let bitmap = NSBitmapImageRep(data:tiff), let png = bitmap.representation(using:.png,properties:[:]) else {
            fputs("Snapshot failed: \(error?.localizedDescription ?? "image export unavailable")\n",stderr);return
        }
        do {
            try png.write(to:URL(fileURLWithPath:output))
            let point = snapshot.point(for:coordinate)
            let meta:[String:Any] = ["source":"Apple MapKit MKMapSnapshotter","name":item.name ?? query,"coordinate":[coordinate.latitude,coordinate.longitude],"appearance":"aqua","logicalSize":[1200,760],"pixelSize":[bitmap.pixelsWide,bitmap.pixelsHigh],"markerPoint":[point.x,point.y],"controls":"not included; any added chrome is a separate reference-inspired overlay"]
            try JSONSerialization.data(withJSONObject:meta,options:[.prettyPrinted,.sortedKeys]).write(to:URL(fileURLWithPath:output+".json"))
            success=true;print("Saved real light Apple map: \(output)")
        } catch { fputs("Save failed: \(error)\n",stderr) }
    }
}
let deadline = Date().addingTimeInterval(55)
while !done && Date()<deadline { RunLoop.current.run(until:Date().addingTimeInterval(0.1)) }
if !done { snapshotter?.cancel();fputs("Timed out\n",stderr) }
if !success { exit(2) }
