"""Easyduino ESP32 case parameters (enclosure-forge target #4).

S1: harness/frontends/kicad_extract.py (KiCad 10 dialect). S2/S3 via the
OpenCodeLM pipe (traces/lm/easyesp32-*). No mounting holes -> pad-and-
rail retention (SimHat-cage class). Literals below are design decisions.
"""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name):
    with open(os.path.join(ROOT, "analysis", name)) as f:
        return json.load(f)


GEOM = _load("pcb_geometry.json")
COMPS = _load("component_geometry.json")

BOARD_W = GEOM["outline"]["w"]          # 28.4
BOARD_L = GEOM["outline"]["h"]          # 47.92
BOARD_T = GEOM["thickness"]             # 1.6

WALL_T = 1.6            # enclosure_design_decision
FLOOR_T = 1.6           # enclosure_design_decision
CORNER_R = 2.5          # enclosure_design_decision

PAD_H = 1.8             # enclosure_design_decision: bare-laminate seat pads
PAD_R = 2.0             # enclosure_design_decision
PADS_UV = [(2.0, 24.5), (26.4, 24.5), (2.0, 45.5), (26.4, 45.5)]  # module/USB clear

RAIL_LIP = 0.8          # enclosure_design_decision: overhang over board edge
RAIL_T = 1.6            # enclosure_design_decision: rail thickness
RAIL_V0, RAIL_V1 = 21.0, 46.0   # band clear of WROOM (v<=19.8) and USB (v>=40.3 at u 9.4..19.1)

RIM_T = 1.0             # enclosure_design_decision: v=0 locator rim
RIM_H = 3.8             # enclosure_design_decision: to just above board top

USB_U = next(c for r, c in COMPS.items()
             if "USB_C" in c["footprint"])["u"]   # derived_kicad
USB_PLUG_W = 9.5        # manufacturer_doc class: USB-C overmold
USB_PLUG_H = 3.5        # manufacturer_doc class
USB_CLEAR = 0.6         # enclosure_design_decision
USB_REACH = 12.0        # enclosure_design_decision

TALLEST = max(c["height"] for c in COMPS.values())
LID_INT_Z = PAD_H + BOARD_T + TALLEST + 1.0

LID_LIP = 1.2           # enclosure_design_decision
LID_GAP = 0.25          # enclosure_design_decision
