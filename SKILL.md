---
name: ground-map-photo-weave
description: Turn a downward-looking shoe-and-ground photo into an Apple Maps inspired ground-plane collage, with a perspective-matched rounded map panel underneath the original shoes and optional location marker. Use for stepping-on-a-map photo edits, not floating travel dashboards.
---

# Ground Map Photo Weave

Keep the supplied photograph full bleed. Insert a rounded landscape map surface into the ground plane, beneath the original shoes. Read [references/composition.md](references/composition.md) before production. A finished reference is visual guidance, never the identity, footwear, ground or location source.

## Fresh-chat reference loading

Before production, read [fresh-chat visual contract](references/fresh-chat-visual-contract.md), inspect the bundled visual reference. For a generative preview, pass it together with the new user source to the image-generation call; for deterministic production, follow the bundled composition/script route and preserve source pixels. Do not assume earlier chat images are visible to the generator. Use this package as the style source; treat custom fields and occlusion choices as per-photo inputs. Read [reference-quality.md](references/reference-quality.md) for proportions, readability and the no-sticker acquisition fallback before composing.

## Inputs
Use a raw downward-looking photograph with visible footwear, legs and enough unobstructed ground. Preserve shoes, socks, trousers, anatomy, pose, sunlight, ground texture and markings. Do not invent feet, change stance or replace the pavement to fit the reference.

Before production, obtain the desired city/neighborhood and acquire a real Apple Maps asset yourself where tools permit. Ask for the location only when missing. A missing screenshot is an acquisition task, not an automatic request for the user to upload one. Read references/apple-assets.md and use Apple Maps on the web as the cross-platform default (Chrome/Edge on Windows or compatible browsers on macOS); use the native Maps app only when available and needed for a closer native-control match; ask for an asset only after explaining a concrete acquisition blocker. Use a screenshot captured from Apple's Maps app/web or an authenticated Apple Maps Snapshot/MapKit output. Do not substitute Google Maps, random internet maps, AI-invented roads, or a fictional unlabeled map without a new explicit user request. Preserve the asset's actual street geometry, names and attribution. A city name is insufficient input for fabricating a map. Do not assume London or infer GPS from footwear. See [references/apple-assets.md](references/apple-assets.md) for verified acquisition options.

For the reference's avatar effect, use a genuine Apple Memoji created in Apple's editor. When the user asks for a red hat or another customization, first check whether the local Apple Messages Memoji editor can create it through available UI tools, then obtain a sticker/image without sending a message or changing the user's profile. Follow the acquisition procedure in references/apple-assets.md. A public default character is acceptable only when its Apple origin and requested appearance can be verified and the user does not request their own likeness. Do not inspect unrelated conversations or privately stored stickers. Do not promise an API, automatic photo conversion, or successful export before actually obtaining the asset. Preserve the obtained face pixels. If the editor/export is inaccessible and a supplied sticker is unavailable, try a verified Apple-published default Memoji before requesting a sticker. Read references/apple-assets.md for the source and acquisition fallback. Do not ask again for a sticker the user has said they cannot provide. Report the actual remaining blocker only after trying applicable acquisition paths. When Memoji is explicitly requested, do not offer generic cartoon/Genmoji or blue-dot substitution repeatedly. The pin bubble is composited UI, not evidence of a native automatic Maps Memoji feature.

Do not invent routes, bookings, GPS history or current location claims. Standard interface labels such as 3D are acceptable; preserve requested place names verbatim.

## Cross-platform map acquisition

This Skill does not require an Apple computer, access to private saved places, GPS permissions or the user's installed map app. The user supplies a city/landmark; the agent obtains a public Apple Maps view through https://maps.apple.com in a supported browser. Windows Chrome/Edge can supply genuine Apple map imagery. Choose the same standard light 2D appearance, region, zoom, orientation and capture aspect across systems, then apply the same composition rules. Do not promise byte-identical rendering or full iPhone app controls from the web map.

For repeated standardized acquisition, use authenticated Maps Web Snapshots/MapKit when credentials are actually configured; this is an optional developer route, not a prerequisite for an ordinary screenshot workflow. No silent purchases or assumed credentials. Native-only controls may be authored as a clearly identified reference-inspired UI overlay; never repaint the underlying roads or call the overlay a native app screenshot.

Memoji availability is separate from map availability. On Windows do not require a nonexistent local Messages editor: use a supplied genuine Memoji or, when a generic character is acceptable, acquire a verified Apple-published default. If neither can be acquired, explain the concrete avatar limitation. An original generated avatar is permitted only when explicitly selected and must not be called Apple Memoji. Map acquisition itself should continue independently.

## Reference style gate
Match the reference map's appearance before compositing: pale road-map palette, light building blocks, flat 2D geometry, restrained labels and compact white controls where shown. A geographically correct dark-mode web map, satellite image, search-results screenshot or rotated north orientation alone does not satisfy this reference. Use the map's own appearance/view controls or another real Apple capture; do not repaint roads or invert a dark screenshot and claim a native light map. Prefer a map-local light option or a real MapKit snapshot with explicit light appearance. If changing global system appearance is necessary, observe the relevant settings authorization requirement and restore its previous value. A prior rejected dark preview is not authorization to keep using dark mode.

Inspect the actual reference image when available. If only a prior written breakdown is available, say that the match is based on that breakdown, rather than claiming visual verification. A raw map capture is an intermediate asset, not the requested photo-weave preview. Do not stop at showing the map unless a concrete blocker prevents composition.

## Layout and production
1. Explain the source-specific plan: map corners/rotation, ground perspective, which shoes overlap it, location label and optional avatar. Use one landscape rounded panel crossing the space between the shoes and beneath at least one natural shoe silhouette. Keep visible ground around it; no phone chassis or photo border.
2. Crop and composite the confirmed REAL Apple Maps asset into the panel; do not redraw its road network or labels with image generation. Prefer native UI captured with the map when matching the reference; recreate only missing interface chrome, never represent a Snapshot as an exact screenshot of all Maps app controls. Optional UI: small binoculars circle on left, 3D circle on right, stacked map/location pill, and a blue dot with a compact avatar pin. Use only what fits without visual clutter. Transform the map and its UI as one coherent plane; do not paste upright screen controls onto a tilted map.
3. Preserve the capture aspect ratio before projection: crop to the desired landscape shape, then resize uniformly; never squeeze a wide/portrait screenshot into an arbitrary panel. Map geometry follows the photographed ground's perspective and rotation. Use restrained foreshortening; a mathematical homography alone is not visual acceptance. Inspect roads, circular controls, avatar face and labels at delivery size; reduce compression or reframe the capture when they appear flattened or unreadable. Retain rounded corners after transformation. Give the panel subtle scene-consistent grounding; no thick extrusion, floating levitation, luminous neon edge or glass refraction. Match photographic exposure and color temperature.
4. Layer order: original photograph -> subtle panel-to-ground shadow if needed -> transformed map/UI -> shoe-to-map shadow -> selected ORIGINAL shoes/socks/legs in foreground. Shoes occlude every intersecting map label, marker and button. Never redraw UI over shoes or move feet to reveal it.
5. Preserve existing source lighting and shadows on exposed ground. Where a shoe now covers the map, add only a restrained matching contact/cast shadow on that map, aligned with the original sun direction; avoid double shadows or dark cutout halos. Shadows should follow actual contact, not imply the map is floating high above asphalt.
6. Produce ONE preview, inspect, then stop for human review. For analysis-only requests, deliver analysis and Skill files without generating. Do not expand to videos, other styles or batches until approved.

Use deterministic perspective compositing, original foreground masks and separately rendered text for source-locked delivery. Image generation can provide an aesthetic preview, but does not prove unchanged source pixels or geographic correctness. Report these limitations explicitly when material.

## Acceptance
- Source footwear, pose and pavement remain recognizable; no fabricated anatomy or changed clothes.
- Map is a rounded landscape surface grounded beneath feet, with coherent perspective across roads, text and controls.
- Shoes cover all intersecting map/UI elements with clean natural edges.
- Contact shadows agree with source light; no floating effect, duplicated shadow or dark outline.
- Map appearance matches the chosen reference, including light/dark mode and 2D presentation;
- Map comes from a real Apple Maps asset; verify source, location, road labels and attribution after compositing.
- Avatar is a genuinely acquired Apple Memoji, or an original AI avatar / blue-dot-only is explicitly chosen; no invented user likeness or fake native integration.
- Readable restrained UI; no visibly stretched map, flattened face or illegible primary place label.
- For the bundled reference look, retain the white avatar bubble and compact white controls when assets permit. A no-avatar/plain-map variant needs an explicit user choice and cannot silently replace a requested avatar.
- No generic scrapbook, phone hardware, unrelated panels or marketing headline.
Deliver the preview and brief findings; structural validation is not human aesthetic approval.

## Author and public reference

Created and maintained by **理智画** (GitHub: [liuzihe849-png](https://github.com/liuzihe849-png)). Inspect [the original sample](assets/reference-original.png) and read [sample scope and limitations](references/public-sample.md). The sample is a visual aid, not a user identity or proof of exact fidelity. Do not copy sample-specific defects into new outputs.

## Mandatory shoe/map quality gate

The current primary reference is [the user-selected clear-street sample](assets/reference-original.png). Before production read [shoe/map quality gate](references/shoe-map-quality.md). Use uniform scale + rotation for near-top-down photos, not an arbitrary trapezoid; run `scripts/check_map_geometry.py` on the actual crop and placement. Make the surface large enough and independently recapture at a readable street zoom. Inspect both original shoe outlines enlarged over light/dark backgrounds, repair coarse masks, and add both visible directional shoe cast shadows and smaller sole contact shadows clipped to the map. Inspect real output at final size; geometry or protected interior pixel success cannot replace edge/shadow/label approval.
