def pickupArea_circ(w_robot,r_circ,mag_c):

    import math
    import numpy as np

    # Circular magnets can be picked-up in 4 different manners:
    # along the radial direction, towards the center of the plate:                                rad_out
    # along the radial direction, away from the center of the plate:                              rad_in
    # tangentially from the radial direction, from the left (looking towards center of plate):    tan_L
    # tangentially from the radial direction, from the right (looking towards center of plate):   tan_R

    # For each possibility a rectangle area is calculated that corresponds to the area needed by the robot arm
    # to pickup the magnets

    # with w_robot the width of the robot arm, r_circ the radius of the circular magnet, mag_c the coordinates
    # of the circular magnet (x_c,y_c,ang_c)

    # Calculate the hypotenuse of the triangle between the center of the circular magnet to the center fo the area
    # and the projected center of the area on the vertical axis
    h = 0.5 * (0.5 * w_robot + r_circ)

    A = []

    i = 0
    for magnet in mag_c:
        x_c = mag_c[i][0]
        y_c = mag_c[i][1]
        ang_c = mag_c[i][2]

        x_area_tan_R = x_c + h * math.sin((np.pi / 180) * (- ang_c))
        y_area_tan_R = y_c + h * math.cos((np.pi / 180) * (- ang_c))

        x_area_tan_L = x_c - h * math.sin((np.pi / 180) * (- ang_c))
        y_area_tan_L = y_c - h * math.cos((np.pi / 180) * (- ang_c))

        x_area_rad_in = x_c + h * math.sin((np.pi / 180) * (90 - ang_c))
        y_area_rad_in = y_c + h * math.cos((np.pi / 180) * (90 - ang_c))

        x_area_rad_out = x_c - h * math.sin((np.pi / 180) * (90 - ang_c))
        y_area_rad_out = y_c - h * math.cos((np.pi / 180) * (90 - ang_c))

        area = [[x_area_tan_R,   y_area_tan_R,   -ang_c],
                [x_area_tan_L,   y_area_tan_L,   -ang_c],
                [x_area_rad_in,  y_area_rad_in,  -ang_c],
                [x_area_rad_out, y_area_rad_out, -ang_c]]

        A.append(area)

        i += 1

    return A
