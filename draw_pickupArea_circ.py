def drawPickupArea_circ(coordinates,l_robot,w_robot,r_circ):
    # draw the different pickup area of the robot arms for the circular magnets
    # with coordinates the coordinates of the areas, l_robot and w_robot the width and length of the robot arm
    # respectively and r_circ the radius of the circular magnet

    from rectangle import drawRect

    i = 0
    for magnet in coordinates:
        [x_tan_L,    y_tan_L,   ang] = coordinates[i][0]
        [x_tan_R,    y_tan_R,   ang] = coordinates[i][1]
        [x_rad_in,   y_rad_in,  ang] = coordinates[i][2]
        [x_rad_out,  y_rad_out, ang] = coordinates[i][3]

        drawRect(x_tan_L,   y_tan_L,   l_robot, (3.0 * w_robot / 2.0) + r_circ, ang, 'y')
        drawRect(x_tan_R,   y_tan_R,   l_robot, (3.0 * w_robot / 2.0) + r_circ, ang, 'y')
        drawRect(x_rad_in,  y_rad_in,  l_robot, (3.0 * w_robot / 2.0) + r_circ, ang, 'y')
        drawRect(x_rad_out, y_rad_out, l_robot, (3.0 * w_robot / 2.0) + r_circ, ang, 'y')

        i += 1