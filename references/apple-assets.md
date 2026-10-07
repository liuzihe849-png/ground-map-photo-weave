# Verified Apple asset workflow

Verified 2026-10-07 against Apple's official documentation.

## Real map
For a one-image production, capture the chosen area in Apple's Maps app on iPhone/Mac, or Apple Maps on the web where available. Keep actual map pixels/labels; hide irrelevant search UI only through deliberate crop, preserve required attribution. Native app screenshot best matches the reference's visible app control style. Capture is an asset-acquisition method, not a blanket statement about publication permissions.

For automated static maps, Apple's Maps Web Snapshots provides region/annotation customization. It requires the appropriate Apple developer authentication/signing setup; do not claim configured access without an actual successful request. MapKit JS provides interactive maps and custom annotations, not automatic access to the user's Memoji. A static map API output does not include every Maps app screen control.

Official sources:
- https://developer.apple.com/maps/web/
- https://developer.apple.com/news/?id=ftkfxb8m

## Memoji
Apple's Messages editor supports creating a personalized Memoji by choosing skin, hairstyle, eyes and more. The created Memoji becomes a sticker pack; choose and share a sticker, then extract that supplied asset for the marker. For static artwork, a sticker is enough; animated capture is unnecessary.

The reference visually resembles a Memoji head in a custom location bubble. Its original author/source layers are unavailable, so this is identification by appearance, not verified provenance or proof of a built-in Maps feature. Do not substitute AI-generated cartoon heads and call them genuine Memoji. No public automation/editor API has been verified in this workflow.

Official source:
- https://support.apple.com/zh-cn/111115

## Intake checklist
Raw shoe/ground photo; selected city/area; genuine Apple Maps screenshot or successfully fetched map asset; user-selected Memoji sticker or explicit blue-dot-only choice. Prepare these before the one-preview generation/compositing stage. Use deterministic compositing for real map and Memoji fidelity; generative edits alone do not establish unchanged map labels or avatar pixels.

## Agent-led acquisition
1. With the user's named city/landmark, search Apple Maps directly and verify the visible place and surrounding roads. Default to Apple Maps on the web for cross-platform use; native Maps is optional when available for a closer reference-control match. Keep location permission off unless needed and authorized; a named landmark does not require the user's GPS.
2. Inspect the map appearance. For this reference, obtain a light standard 2D map through available map appearance controls. Do not deliver a dark screenshot merely because search succeeded. Set a landscape region with enough road detail and retain attribution in the eventual panel. Store the capture and source URL/app context.
3. For genuine Memoji, check the local Messages sticker/Memoji editor using UI tools. Apple's documentation supports creating Memoji on Mac; actual availability, red-hat choices and export must be verified on the installed version. Use a blank draft, do not select unrelated conversations, send a message, edit existing personal Memoji, or change contact/account photos. Create a separate character when available and select the requested headwear/color. Capture/export only the requested sticker if the UI supports it; saving a character is not proof of a usable image export.
4. If login, editor access or safe export blocks acquisition, and the user does not need their likeness, try a verified Apple-published default from the source below. If the user cannot supply a sticker, do not ask repeatedly or silently omit the avatar. Request a sticker only if the applicable editor and public-source paths cannot satisfy the appearance requirement. Never substitute a generated lookalike and call it Apple Memoji.
5. Before composing, inspect both map and avatar assets, then produce one ground-plane photo preview. Record failed acquisition honestly; editing this workflow does not establish successful production.

Official Mac guide: https://support.apple.com/guide/messages/ichtb967d30b/mac

## Windows and portable acquisition
Apple officially lists Chrome and Edge for Maps on the web on Mac/Windows. Use https://maps.apple.com; verify browser loading, searched area, light standard 2D mode and actual map labels. User GPS or a personal Apple map library is unnecessary for a named region. Capture the same region/zoom/orientation/aspect to reduce cross-platform differences, while acknowledging that web/native versions can differ in cartography details and UI.

Official compatibility source, checked 2026-10-07: https://support.apple.com/en-ie/120585

For automated standardized captures, Apple's authenticated Web Snapshots is optional. Token creation is documented at https://developer.apple.com/documentation/MapKitJS/creating-a-maps-token . Do not imply that a token exists, the service has been tested, or setup has no account requirements.

On Windows, personalized Memoji creation/export is a separate Apple-device asset step. A verified Apple-published default can supply the generic avatar effect without an Apple device. Try that path when the user has no sticker and does not need their likeness; do not block map acquisition or fabricate native Memoji provenance. An explicitly selected original AI avatar remains a custom avatar.

## Verified public default Memoji fallback

Apple Newsroom's “Apple previews iOS 12” publishes a selection of 12 Memojis: https://www.apple.com/newsroom/2018/06/apple-previews-ios-12/ . The linked image is https://www.apple.com/newsroom/images/product/os/ios/standard/ios12_apple-memoji_06042018_big.jpg.large.jpg .

The public package does not bundle an Apple Memoji sticker or claim an exported native character. Acquire a genuine Apple-published asset through the source above when the requested generic appearance matches, or obtain a user-provided native export. Preserve the acquired source pixels and record provenance for that actual acquisition. The original blue-cap avatar visible in assets/reference-original.png is AI-generated by explicit user selection, not Apple Memoji. Do not infer that source provenance grants unrestricted reuse rights.

## Native MapKit light snapshot fallback on macOS

When browser appearance is dark and native UI control is inaccessible, a native MapKit snapshot can request `NSAppearance(named: .aqua)` without changing the system. This is Apple-rendered map imagery, not a recolored screenshot and not a capture of full Maps app chrome. Use [capture-mapkit.swift](../scripts/capture-mapkit.swift) where Swift and MapKit are available. No assumed Web Snapshots token is needed for this native route. It is not a Windows solution.

Example (supply a verified exact result name and regional search hint for each task):

```sh
swift scripts/capture-mapkit.swift '成都国际金融中心' 30.658 104.07906 /absolute/path/map.png
```

The helper searches the named landmark, uses an exact-name MapKit result, captures a light standard landscape map, and writes coordinate/pixel metadata. If it lists candidates or fails, resolve the actual place; do not select an unrelated first result. Search coordinates from Apple web should be treated as hints, not blindly reused as native landmark coordinates: the observed web “Chengdu IFS” result referred to an Apple office/tower, while native exact search found 成都国际金融中心. Verify the snapshot's actual IFS/红星路/太古里 labels before positioning the avatar. Use snapshot.point(for:) for the selected MapKit coordinate.

Observed 2026-10-07: native interface capture failed with ScreenCaptureKit errors even after a REPL reset, but native MKMapSnapshotter successfully produced a real 1200×760 light map. Do not make this local UI failure a requirement for other machines or repeatedly retry the same failed control path.

Official APIs: https://developer.apple.com/documentation/mapkit/mkmapsnapshotter and https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/appearance .
