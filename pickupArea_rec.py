def pickupArea_rec(w_robot,l_robot,l_rect,mag):

    import math
    import numpy as np

    # Rectangular magnets can be picked-up in 2 different manners:
    # towards the circular magnet:                                in
    # away from the circular magnet:                              out

    # For each possibility a rectangle area is calculated that corresponds to the area needed by the robot arm
    # to pickup the magnets

    # with w_robot the width of the robot arm, l_robot, w_robot the length and width of the robot arm respectively,
    # mag_r the coordinates of the rectangular magnets (x_r,y_r,ang_r)

    # Calculate the hypotenuse of the triangle between the center of the rectangular magnet to the center fo the area
    # and the projected center of the area on the vertical axis - See Tiph's notes
    h = 0.25 * (l_rect + w_robot)

    x_r   = mag[0]
    y_r   = mag[1]
    ang_r = mag[2]

    # Calculate the center of the pickup area
    x_out = x_r + h * math.sin((np.pi / 180.0) * (ang_r))
    y_out = y_r + h * math.cos((np.pi / 180.0) * (ang_r))

    x_in = x_r - h * math.sin((np.pi / 180.0) * (ang_r))
    y_in = y_r - h * math.cos((np.pi / 180.0) * (ang_r))

    area = [[x_out, y_out, ang_r],
            [x_in,  y_in,  ang_r]]

    return area


