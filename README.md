# Easyduino ESP32 Case — enclosure-forge target #4

Parametric 3D-printable case for the
[Easyduino ESP32](https://github.com/Hanqaqa/Easyduino) open devkit
(28.4 × 47.92 mm, USB-C, ESP32-WROOM-32E, **no mounting holes**).
Built by the enclosure-forge harness: generic KiCad-10 front-end
extraction (incl. the board-frame-footprint outline trick), S2/S3 via
the OpenCodeLM pipe (traces in the forge), pad-and-rail retention,
boolean gate.

## Design
- **Pad-and-rail retention** (SimHat-cage class): 4 bare-laminate pads,
  friction rails on both long walls (lips clamp the board edges from
  above), v=0 locator rim ahead of the WROOM antenna.
- USB-C opening through the v-max wall: seated-plug envelope + bend
  void, zero shell material (boolean-checked).
- 7/7 checks PASS incl. component clearance vs all 29 extracted parts
  and deterministic rebuild. Report: `analysis/interference_report.json`.

## Regenerate
```sh
python3 scripts/validate.py && python3 scripts/build.py
```

## Before printing
Rail-clamp feel is printer-dependent: print the case, check slide-in
force; sand or shim the 0.8 mm lips. WROOM antenna faces the plastic
rim (no metal nearby; RF range unmeasured — see forge MEASUREMENTS
convention). Verify USB-C reach with a real cable boot.

## 3D

- Spin the assembly: [`exports/easyduino-esp32_assembly.glb`](exports/easyduino-esp32_assembly.glb) (GLB — Windows 3D Viewer, macOS
  Preview, Blender, gltf-viewer.donmccurdy.com). STLs in
  `output/exports/` render inline on GitHub.
- Scored by the forge metric: **1.00 (7/7 checks)** — see
  `Amperstrand/enclosure-forge` experiments/runs/.

