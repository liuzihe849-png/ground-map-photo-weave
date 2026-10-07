# Shoe-on-map production gate

Primary reference: `../assets/reference-original.png`, explicitly selected by the user. Match its large, readable, undistorted surface and directional shoe shadows. Beijing, pale clothes and blue-cap avatar are example data, not defaults for new users. The sample itself is not verified map source data: obtain a fresh genuine Apple capture for the requested location.

## Map size versus map zoom

These are separate decisions. Make the panel large enough to read, normally around 75–95% of image width when the available ground supports it, with both original shoes intersecting naturally. Do not enlarge or reposition the feet. Independently zoom/reframe the actual Apple map capture to show the local streets around the requested landmark. Enlarging a low-resolution whole-city screenshot does not make its labels legible.

At final delivery size, identify at least two unobscured real street names and the intended landmark/neighborhood if it is present in the capture. If labels are too small, crowded or hidden, recapture at closer zoom, filter irrelevant POIs where the real map supports it, or reframe. Do not rewrite street labels or fabricate a missing landmark. Keep legal attribution visible and do not crop it away just to simplify the UI.

## Geometry before placement

For near-top-down ground photographs, default to **uniform scale + in-plane rotation** of one rounded landscape map/UI surface. A rotated rectangle is not a trapezoid. Do not squeeze x and y separately, skew its sides or apply a four-corner homography merely because the map belongs on the ground. Mild perspective is permitted only when the actual new camera angle requires it and controls/labels remain recognizable.

Record a JSON plan containing `map_crop_size: [width,height]`, `corners: [[TLx,TLy],[TRx,TRy],[BRx,BRy],[BLx,BLy]]` and `projection: "uniform-rotate"` or `"mild-perspective"`. For the latter add an observed `camera_reason`. Before rendering, run:

```sh
python scripts/check_map_geometry.py plan.json --output geometry-qc.json
```

A failed check requires corrected crop/placement, not a changed threshold to make that image pass. The tolerances are safeguards for this reference style, not a universal camera-calibration model. Geometry passing cannot certify aesthetics.

## Shoe edge matte

Use the original foreground pixels and a full-resolution segmentation/trimmed matte. A coarse polygon is a planning aid, not a finished shoe outline. Follow the real toe curve, outsole edge, heel, trouser hem and any visible laces. Keep pavement outside the silhouette out of the foreground layer. Avoid cutting away dark rubber just because it resembles the road.

Inspect BOTH shoes at 200–400% over temporary light and dark backgrounds, then inspect at final size over the map. Reject stair steps, straight polygon chords through rounded toes, background slivers, white fringes, dark halos and clipped soles. Use a narrow antialiased transition rather than broad blur. Repair the matte before adding shadows; shadows cannot hide a bad cutout. Preserve every visible part of the original shoes and pants.

## Shoe-to-map shadows

Infer sunlight direction and softness from actual ground shadows. On the map, add a **directional soft cast shadow** extending opposite the sun, plus a **smaller contact shadow** close to the sole. A uniform blurred outline around the whole leg is not a cast shadow. Offset, blur and opacity depend on the photo; do not copy fixed offsets from the reference into every new source.

Clip both shadow components to the visible map surface and place them below restored original shoes but above map/UI. Keep the surrounding pavement's original shadows. The shoe shadow must continue naturally across the map boundary without duplicate darkening; avoid heavy all-around black edging or a card hovering above the ground. At delivery size the shadow must remain visibly readable against the pale map and must not erase the street labels wholesale.

## Actual-output acceptance record

After opening the final image, record: genuine map source/region and capture zoom; geometry result; two readable street labels; two shoe-edge closeups; cast-shadow direction and contact-shadow presence; remaining uncertainties. Do not declare the edit accepted when only protected interior pixels match, files validate or a script exits successfully. Return one preview for the user's aesthetic review.
