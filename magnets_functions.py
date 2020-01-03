from basic_computations import drawRect, calculate_rectangle_center_xy_coordinates, calculate_circle_xy_coordinates
import numpy as np
import math
import matplotlib.pyplot as plt

def drawPickupArea_circ(coordinates,l_robot,w_robot,r_circ):
    '''
    draw the different pickup area of the robot arms for the circular magnets
    with coordinates the coordinates of the areas, l_robot and w_robot the width and length of the robot arm
    respectively and r_circ the radius of the circular magnet
    '''

    [x_tan_L,   y_tan_L,   ang] = coordinates[0]
    [x_tan_R,   y_tan_R,   ang] = coordinates[1]
    [x_rad_in,  y_rad_in,  ang] = coordinates[2]
    [x_rad_out, y_rad_out, ang] = coordinates[3]

    drawRect(x_tan_L,   y_tan_L,   l_robot, (3.0 * w_robot / 2.0) + r_circ, ang, 'y')
    drawRect(x_tan_R,   y_tan_R,   l_robot, (3.0 * w_robot / 2.0) + r_circ, ang, 'y')
    drawRect(x_rad_in,  y_rad_in,  l_robot, (3.0 * w_robot / 2.0) + r_circ, ang, 'y')
    drawRect(x_rad_out, y_rad_out, l_robot, (3.0 * w_robot / 2.0) + r_circ, ang, 'y')


def drawPickupArea_rect(coordinates,l_robot,w_robot,l_rect):
    '''
    draw the different pickup area of the robot arms for the circular magnets

    :param coordinates: coordinates of the areas
    :param l_robot: robot arm length
    :param w_robot: robot arm width
    :param l_rect: length of the rectangular magnet

    '''

    [x_out, y_out, ang_r] = coordinates[0]
    [x_in,  y_in,  ang_r] = coordinates[1]

    drawRect(x_out, y_out, l_robot, 0.5 * (l_rect + 3.0 * w_robot), ang_r, 'c')
    drawRect(x_in,  y_in,  l_robot, 0.5 * (l_rect + 3.0 * w_robot), ang_r, 'c')


def draw_robot_arm(mag, w_robot, l_robot):
    '''
    Draw the robot arm on top of the magnets (two orientation possible for the circular magnets)

    :param mag: coordinates (x,y,orientation angle) of the magnet
    :param w_robot: width of the robot arm
    :param l_robot: length of the robot arm
    :return:
    '''

    i = 0
    for magnet in mag:

        if magnet[3] == 0:
            x_c = mag[i][0]
            y_c = mag[i][1]
            ang_c = mag[i][2]

            # Draw the robot arm on top of the circular magnets (two orientation possible: radial/tangential)
            # circ_robot = drawRect(x1, y1, w_robot, l_robot, 90, 'm')
            drawRect(x_c, y_c, w_robot, l_robot, - ang_c, 'c')
            drawRect(x_c, y_c, w_robot, l_robot, - ang_c + 90, 'c')

        if magnet[3] == 1:
            x_r = mag[i][0]
            y_r = mag[i][1]
            ang_r = mag[i][2]

            # Draw the robot arm on top of the rect. magnets
            drawRect(x_r, y_r, w_robot, l_robot, ang_r + 90, 'c')

        i += 1


def extract_positions(probe,x,y,angs_azAng,L):
    '''
    Extract the coordinates of the magnets

    :param probe:
    :param x: coordinates of the circular magnet
    :param y: coordinates of the circular magnet
    :param angs_azAng: angle of the rectangular magnet
    :param L:
    :return:
    '''

    mag_c = []
    mag_r = []

    for i in probe:

        # Get circular magent's center x and y positions
        x_c = x[int(i) - 1] * 260.0
        y_c = y[int(i) - 1] * 260.0

        # Calculate the angle of the radius (containing the circular magnet)
        if x_c and y_c > 0:
            rot_angle = math.atan(np.abs(y_c / x_c))
        if x_c < 0 and y_c > 0:
            rot_angle = np.pi - math.atan(np.abs(y_c / x_c))
        if x_c < 0 and y_c < 0:
            rot_angle = np.pi + math.atan(np.abs(y_c / x_c))
        if x_c > 0 and y_c < 0:
            rot_angle = 2 * np.pi - math.atan(np.abs(y_c / x_c))
        # Convert into degrees
        angle = rot_angle * (180 / np.pi)

        mag_c.append([x_c, y_c,angle,0,probe[int(i)-1]])

        # From the file fetch the angle of the rectangular magnet (angle relative to the tangent of the radius -
        # See Olivia's notes for details)
        theta = angs_azAng[int(i) - 1] * (180 / np.pi) + 90

        # The angle of the rectangular magnet (absolute)
        alpha = angle + theta - 90

        [x_r, y_r] = calculate_rectangle_center_xy_coordinates(x_c, y_c, L, alpha)

        ang_r = 90 - alpha

        mag_r.append([x_r,y_r,ang_r,1,probe[int(i)-1]])

    return mag_c, mag_r


def pickupArea_circ(w_robot,r_circ,mag):
    '''
    Circular magnets can be picked-up in 4 different manners:
    along the radial direction, towards the center of the plate:                                rad_out
    along the radial direction, away from the center of the plate:                              rad_in
    tangentially from the radial direction, from the left (looking towards center of plate):    tan_L
    tangentially from the radial direction, from the right (looking towards center of plate):   tan_R

    For each possibility a rectangle area is calculated that corresponds to the area needed by the robot arm
    to pickup the magnets

    :param w_robot: width of the robot arm
    :param r_circ: radius of the circular magnet
    :param mag: oordinates of the circular magnet (x_c,y_c,ang_c)
    :return:
    '''

    # Calculate the hypotenuse of the triangle between the center of the circular magnet to the center fo the area
    # and the projected center of the area on the vertical axis
    h = 0.5 * (0.5 * w_robot + r_circ)

    x_c   = mag[0]
    y_c   = mag[1]
    ang_c = mag[2]

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

    return area


def pickupArea_rec(w_robot,l_robot,l_rect,mag):
    '''
    Rectangular magnets can be picked-up in 2 different manners:
    towards the circular magnet:                                in
    away from the circular magnet:                              out

    For each possibility a rectangle area is calculated that corresponds to the area needed by the robot arm
    to pickup the magnets

    :param w_robot: width of the robot arm
    :param l_robot: length of the robot arm
    :param l_rect: length of the rectangular magnet
    :param mag: coordinates of the rectangular magnet (x_r,y_r,ang_r)
    :return:
    '''

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


def plot_magnets(r_circ,w_rect,l_rect,mag,c):
    '''
    plots the magnets

    :param r_circ: radius of the circular magnets
    :param w_rect: width of the rectangular magnets
    :param l_rect: length of the rectangular magnets
    :param mag: coordinates of the magnets (x,y and orientation angle, 0: circ or 1:rect)
    :param c: colour for plotting
    :return:
    '''

    i = 0
    for magnet in mag:

        if magnet[3] == 0:
            # Plot the circular magnets
            x_c = mag[i][0]
            y_c = mag[i][1]

            magnet_circ = calculate_circle_xy_coordinates(x_c, y_c, r_circ)

            plt.plot(magnet_circ[0], magnet_circ[1], c)
            plt.plot(magnet_circ[0], magnet_circ[2], c)

        if magnet[3] == 1:
            # Plot the rectangular magnet
            x_r   = mag[i][0]
            y_r   = mag[i][1]
            ang_r = mag[i][2]

            drawRect(x_r, y_r, w_rect, l_rect, ang_r, c)

        i += 1


def plot_plate(HECTOR_plate):
    '''
    plots HECTOR plate
    '''

    plt.figure()

    # Plot the plate
    plt.plot(HECTOR_plate[0], HECTOR_plate[1], 'r')
    plt.plot(HECTOR_plate[0], HECTOR_plate[2], 'r')
    plt.plot(0, 0, 'x')

    plt.axis('scaled')
    plt.axis([-270, 270, -270, 270])
    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.show()