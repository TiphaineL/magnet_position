def plot_plate_with_magnets(r_circ,w_rect,l_rect,g,L,HECTOR_plate,l_robot,w_robot,
                            probe, x, y, radius, angs, azAngs, angs_azAng):


    import matplotlib.pyplot as plt
    from circle import circle
    import math
    import numpy as np
    from rectangleCenter import rect_center
    from rectangle import drawRect

    plt.figure()

    # Plot the plate
    plt.plot(HECTOR_plate[0], HECTOR_plate[1], 'r')
    plt.plot(HECTOR_plate[0], HECTOR_plate[2], 'r')
    plt.plot(0, 0, 'x')

    for i in probe:

        # Plot the circular magnets
        x1 = x[int(i) - 1] * 260.0
        y1 = y[int(i) - 1] * 260.0

        magnet_circ = circle(x1, y1, r_circ)

        plt.plot(magnet_circ[0], magnet_circ[1], 'r')
        plt.plot(magnet_circ[0], magnet_circ[2], 'r')

        # Plot the rectangular magnets
        # Calculate the angle of the circular magnet (to the center of the plate)
        if x1 and y1 > 0:
            rot_angle = math.atan(np.abs(y1 / x1))
        if x1 < 0 and y1 > 0:
            rot_angle = np.pi - math.atan(np.abs(y1 / x1))
        if x1 < 0 and y1 < 0:
            rot_angle = np.pi + math.atan(np.abs(y1 / x1))
        if x1 > 0 and y1 < 0:
            rot_angle = 2 * np.pi - math.atan(np.abs(y1 / x1))
        # Convert into degrees
        angle = rot_angle * (180 / np.pi)

        # From the file fetch the angle of the rectangular magnet (angle relative to the tangent of the radius -
        # See Olivia's notes for details)
        theta = angs_azAng[int(i) - 1] * (180 / np.pi) + 90

        # the angle of the rectangular magnet (absolute)
        alpha = angle + theta - 90

        # Find the center of the rectangular magnets
        [x2, y2] = rect_center(x1, y1, L, alpha)

        # Draw the rectangular magnets
        drawRect(x2, y2, w_rect, l_rect, 90 - angle + 90 - theta, 'r')
        # rect_magnets = drawRect(x2,y2,w_rect,l_rect,0, 'r')

        # Draw the robot arm on top of the rect. magnets
        # drawRect(x2, y2, w_robot, l_robot, 90 - angle + 90 - theta + 90, 'c')

        # Draw the robot arm on top of the circular magnets (two orientation possible: radial/tangential)
        # circ_robot = drawRect(x1, y1, w_robot, l_robot, 90, 'm')
        # circ_robot   = drawRect(x1, y1, w_robot, l_robot, - angle,      'c')
        # circ_robot_2 = drawRect(x1, y1, w_robot, l_robot, - angle + 90, 'c')

        # Calculate the center and dimension of the shaded area (the whole area the robot arm needs to pick up the magnet)
        # First calculate the hypotenuse (the triangle formed between the center of the rect. magnet,
        # the center of the shaded area and the projection of this latest on the vertical axis) - See Tiph's notes
        h = 0.25 * (l_rect + w_robot)

        # Second calculate the center of the shaded area
        # The pick-up arm can come towards the circular magnet (_out), or away (_in)
        x_shade_out = x2 + h * math.sin((np.pi / 180.0) * (90 - angle + 90 - theta))
        y_shade_out = y2 + h * math.cos((np.pi / 180.0) * (90 - angle + 90 - theta))

        x_shade_in = x2 - h * math.sin((np.pi / 180.0) * (90 - angle + 90 - theta))
        y_shade_in = y2 - h * math.cos((np.pi / 180.0) * (90 - angle + 90 - theta))

        drawRect(x_shade_out, y_shade_out, l_robot, 0.5 * (l_rect + 3.0 * w_robot), 90 - angle + 90 - theta, 'c')
        drawRect(x_shade_in, y_shade_in, l_robot, 0.5 * (l_rect + 3.0 * w_robot), 90 - angle + 90 - theta, 'c')

        # TEST PLOT SHADED AREA OVER CIRCLES

        h = 0.5 * (0.5 * w_robot + r_circ)

        x_shade_tang_right = x1 + h * math.sin((np.pi / 180) * (- angle))
        y_shade_tang_right = y1 + h * math.cos((np.pi / 180) * (- angle))

        x_shade_tang_left = x1 - h * math.sin((np.pi / 180) * (- angle))
        y_shade_tang_left = y1 - h * math.cos((np.pi / 180) * (- angle))

        x_shade_rad_pos = x1 + h * math.sin((np.pi / 180) * (90 - angle))
        y_shade_rad_pos = y1 + h * math.cos((np.pi / 180) * (90 - angle))

        x_shade_rad_neg = x1 - h * math.sin((np.pi / 180) * (90 - angle))
        y_shade_rad_neg = y1 - h * math.cos((np.pi / 180) * (90 - angle))

        drawRect(x_shade_tang_left, y_shade_tang_left, l_robot, (3.0 * w_robot / 2.0) + r_circ, - angle, 'y')
        drawRect(x_shade_tang_right, y_shade_tang_right, l_robot, (3.0 * w_robot / 2.0) + r_circ, - angle, 'y')
        drawRect(x_shade_rad_neg, y_shade_rad_neg, l_robot, (3.0 * w_robot / 2.0) + r_circ, -angle, 'y')
        drawRect(x_shade_rad_pos, y_shade_rad_pos, l_robot, (3.0 * w_robot / 2.0) + r_circ, -angle, 'y')

    plt.axis('scaled')
    plt.axis([-270, 270, -270, 270])
    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.show()