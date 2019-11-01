def draw_robot_arm(mag_c,mag_r,w_robot,l_robot):
    # Draw the robot arm on top of the magnets (two orientation possible for the circular magnets)
    # with mag_c and mag_r the coordinates (x,y,orientation angle) of the circular and rectangular magnet respectively,
    # w_robot and l_robot the width and length of the robot arm
    
    from rectangle import drawRect

    i = 0
    for magnet in mag_c:

        x_c   = mag_c[i][0]
        y_c   = mag_c[i][1]
        ang_c = mag_c[i][2]

        x_r   = mag_r[i][0]
        y_r   = mag_r[i][1]
        ang_r = mag_r[i][2]


        # Draw the robot arm on top of the rect. magnets
        drawRect(x_r, y_r, w_robot, l_robot, ang_r + 90, 'c')

        # Draw the robot arm on top of the circular magnets (two orientation possible: radial/tangential)
        # circ_robot = drawRect(x1, y1, w_robot, l_robot, 90, 'm')
        drawRect(x_c, y_c, w_robot, l_robot, - ang_c,      'c')
        drawRect(x_c, y_c, w_robot, l_robot, - ang_c + 90, 'c')

        i += 1