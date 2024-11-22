;
; Mesh Bed Leveling (mbl)
;
M84 E ; turn off E motor
G29 P1 ; invalidate mbl & probe print area
G29 P1 X0 Y0 W50 H20 C ; probe near purge place
G29 P3.2 ; interpolate mbl probes
G29 P3.13 ; extrapolate mbl outside probe area
G29 A ; activate mbl

;
; Prepare for purge
;
M104 S230
G0 X0 Y-4 Z15 F4800 ; move away and ready for the purge
M109 S230
G92 E0
M569 S0 E ; set spreadcycle mode for extruder

;
; Extrude purge line
;
G92 E0 ; reset extruder position
G1 E2 F2400 ; deretraction after the initial one before nozzle cleaning
G0 E7 X15 Z0.2 F500 ; purge
G0 X25 E4 F500 ; purge
G0 X35 E4 F650 ; purge
G0 X45 E4 F800 ; purge
G0 X48 Z0.05 F8000 ; wipe, move close to the bed
G0 X51 Z0.2 F8000 ; wipe, move quickly away from the bed

;
; Prepare for printing
;
G92 E0
M221 S100 ; set flow to 100%
G21 ; set units to millimeters
G90 ; use absolute coordinates
M83 ; use relative distances for extrusion
M572 S0.036 ; Filament gcode