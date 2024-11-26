import fullcontrol as fc

design_name = "test"

printer_name='prusa_i3'
nozzle_temp = 230
bed_temp = 60
print_speed = 1000
fan_percent = 100

extrusion_width = 0.4
extrusion_height = 0.2
initial_z = extrusion_height * 0.6

layers = 20

bed_dimensions = ( 250, 210, 210 )

if __name__ == '__main__':
    print("Generating gcode...")
    
    steps = []
    for layer in range(layers):
        steps.append(fc.Point(x=50, y=50, z=initial_z+layer*extrusion_height))
        steps.append(fc.Point(x=100, y=50, z=initial_z+layer*extrusion_height))
        steps.append(fc.Point(x=100, y=100, z=initial_z+layer*extrusion_height))
        steps.append(fc.Point(x=50, y=100, z=initial_z+layer*extrusion_height))
        steps.append(fc.Point(x=50, y=50, z=initial_z+layer*extrusion_height))

    # instead of the above for-loop code, you can create the exact same design using built-in FullControl functions (uncomment the next two lines):
    # rectangle_steps = fc.rectangleXY(fc.Point(x=50, y=50, z=initial_z), 50, 50)
    # steps = fc.move(rectangle_steps, fc.Vector(z=EH), copy=True, copy_quantity=layers)

    # preview the design
    fc.transform(steps, 'plot', fc.PlotControls(style='line', zoom=0.7))

    #   generate and save gcode
    gcode_controls = fc.GcodeControls(
        printer_name=printer_name,

        initialization_data={
            'primer': 'front_lines_then_y',
            'print_speed': print_speed,
            'nozzle_temp': nozzle_temp,
            'bed_temp': bed_temp,
            'fan_percent': fan_percent,
            'extrusion_width': extrusion_width,
            'extrusion_height': extrusion_height})
    
    gcode = fc.transform(steps, 'gcode', gcode_controls)
    open(f'{design_name}.gcode', 'w').write(gcode)