;FLAVOR:Marlin

M140 S50
M105
M190 S50
M104 S200
M105
M109 S200
M82 ;absolute extrusion mode

; Ender 3 Custom Start G-code
G92 E0                          ; Reset Extruder
G28                             ; Home all axes
G1 Z2.0 F3000                   ; Move Z Axis up little to prevent scratching of Heat Bed
G1 X0.1 Y20 Z0.3 F5000.0        ; Move to start position
G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line
G1 X0.4 Y200.0 Z0.3 F5000.0     ; Move to side a little
G1 X0.4 Y20 Z0.3 F1500.0 E30    ; Draw the second line
G92 E0                          ; Reset Extruder
G1 Z2.0 F3000                   ; Move Z Axis up little to prevent scratching of Heat Bed
G1 X5 Y20 Z0.3 F5000.0          ; Move over to prevent blob squish
G92 E0
G1 F2700 E-5

;----------------------------------------------------------------
