def drawPickupArea_rect(coordinates,l_robot,w_robot,l_rect):
    # draw the different pickup area of the robot arms for the circular magnets
    # with coordinates the coordinates of the areas, l_robot and w_robot the width and length of the robot arm
    # respectively and r_circ the radius of the circular magnet

    from rectangle import drawRect

    [x_out, y_out, ang_r] = coordinates[0]
    [x_in,  y_in,  ang_r] = coordinates[1]

    drawRect(x_out, y_out, l_robot, 0.5 * (l_rect + 3.0 * w_robot), ang_r, 'c')
    drawRect(x_in,  y_in,  l_robot, 0.5 * (l_rect + 3.0 * w_robot), ang_r, 'c')