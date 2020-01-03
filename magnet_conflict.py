import numpy as np
import matplotlib.pyplot as plt
from basic_computations import calculate_circle_xy_coordinates, rectangle_corner
from magnets_functions import pickupArea_circ, pickupArea_rec


def circle_segment_intersection(x0,y0,x1,y1,x2,y2,r):
    '''
    Find if a segment intersect a circle by solving a quadratic parametric equation a*t^2 + b*t + c = 0

    :param x0: coordinates of the center of the circle
    :param y0: coordinates of the center of the circle
    :param x1: coordinates of the start point of the segment
    :param y1: coordinates of the start point of the segment
    :param x2: coordinates of the end point of the segment
    :param y2: coordinates of the end point of the segment
    :param r: adius of the circle
    :return: True or False
    '''

    dx = x2 - x1
    dy = y2 - y1

    fx = x1 - x0
    fy = y1 - y0

    A = dx**2 + dy**2
    B = 2*( dx*fx + dy*fy )
    C = fx**2 + fy**2 - r**2

    Delta = B**2 - 4*A*C

    t1 = (-B + np.sqrt(Delta)) / (2 * A)
    t2 = (-B - np.sqrt(Delta)) / (2 * A)

    x_intersection_1 = x1 + t1 * dx
    y_intersection_1 = y1 + t1 * dy

    x_intersection_2 = x1 + t2 * dx
    y_intersection_2 = y1 + t2 * dy

    intersection = False

    if Delta >= 0:
        if min(x1,x2) <= x_intersection_1 <= max(x1,x2):
            intersection = True
        if min(x1,x2) <= x_intersection_2 <= max(x1,x2):
            intersection = True
    magnet_circ = calculate_circle_xy_coordinates(x0, y0, r)

    plt.plot([x1,x2],[y1,y2])
    plt.plot(magnet_circ[0], magnet_circ[1], 'c')
    plt.plot(magnet_circ[0], magnet_circ[2], 'c')
    if intersection:
        plt.plot(x_intersection_1,y_intersection_1,'xr')
        plt.plot(x_intersection_2,y_intersection_2,'xr')
    plt.axis('scaled')

    return intersection


def circle_rect_intersection(x_r,y_r,ang_r,l,w,x_c,y_c,r):
    '''
    check the intersection of a circle with a rectangle, by iterating through every segments of the rectangle

    :param x_r: coordinates of the center of the rectangle
    :param y_r: coordinates of the center of the rectangle
    :param ang_r: orientation of the rectangle (along the vertical axis)
    :param l: length of the rectangle
    :param w: width of the rectangle
    :param x_c: coordinate of the center of the circle
    :param y_c: coordinate of the center of the circle
    :param r: radius of the circle
    :return:
    '''

    # Calculate the coordinates of the corners of the rectangle (4 corners)
    corner_rect = rectangle_corner(x_r,y_r,l,w,ang_r)

    #circ = circle(x_c, y_c,r)

    #plt.plot(circ[0], circ[1], 'c')
    #plt.plot(circ[0], circ[2], 'c')

    for k,l in zip([0,1,2,3],[1,2,3,0]):

        x1 = corner_rect[k][0]
        y1 = corner_rect[k][1]

        x2 = corner_rect[l][0]
        y2 = corner_rect[l][1]

        intersection = circle_segment_intersection(x_c, y_c, x1, y1, x2, y2, r)

    return intersection


def segments_intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    '''
    Check if two segments intersect

    :param x1: Segment 1 starting point x
    :param y1: Segment 1 starting point y
    :param x2: Segment 1 ending point x
    :param y2: Segment 1 ending point y
    :param x3: Segment 2 starting point x
    :param y3: Segment 2 starting point y
    :param x4: Segment 2 ending point x
    :param y4: Segment 2 ending point y
    :return: True or False
    '''

    def line_param(x1, y1, x2, y2):
        slope = (y2 - y1) / (x2 - x1)
        origin = y2 - slope * x2
        return slope, origin

    intersect = False

    # Check if vertical line (if vertical line: it's not possible to compute the slope)
    if x1 == x2:
        m,o = line_param(x3,y3,x4,y4)
        fc = m * x1 + o
        if min(y1,y2) <= fc <= max(y1,y2):
            intersect = True

            intersect_x = x1
            intersect_y = fc

    elif x3 == x4:
        m,o = line_param(x1,y1,x2,y2)
        fc = m * x3 + o
        if min(y3,y4) <= fc <= max(y3,y4):
            intersect = True

            intersect_x = x3
            intersect_y = fc

    else:
        m1, o1 = line_param(x1, y1, x2, y2)
        m2, o2 = line_param(x3, y3, x4, y4)


        if m1 != m2:

            intersect_x = (o2 - o1) / (m1 - m2)
            intersect_y = m1 * intersect_x + o1

            if min(x1,x2) <= intersect_x <= max(x1,x2):
                if min(x3,x4) <= intersect_x <= max(x3,x4):
                    intersect = True

    import matplotlib.pyplot as plt
    plt.plot([x1, x2], [y1, y2], 'b')
    plt.plot([x3, x4], [y3, y4], 'b')
    if intersect:
        plt.plot(intersect_x, intersect_y, 'xb')

    return intersect


def rect_rect_intersection(x_1,y_1,ang_1,l_1,w_1,x_2,y_2,ang_2,l_2,w_2):
    '''
    check the intersection of a rectangle with a rectangle, by iterating through every pair of segments from rectangle 1
    and of rectangle 2

    :param x_1: coordinates of the center of the rectangle 1
    :param y_1: coordinates of the center of the rectangle 1
    :param ang_1: orientation of the rectangle 1 (along the vertical axis)
    :param l_1: length of the rectangle 1
    :param w_1: width of the rectangle 1
    :param x_2: coordinates of the center of the rectangle 2
    :param y_2: coordinates of the center of the rectangle 2
    :param ang_2: orientation of the rectangle 2 (along the vertical axis)
    :param l_2: length of the rectangle 2
    :param w_2: width of the rectangle 2
    :return:
    '''

    # Calculate the coordinates of the corners of the rectangle (4 corners)
    corner_rect_1 = rectangle_corner(x_1,y_1,l_1,w_1,ang_1)
    corner_rect_2 = rectangle_corner(x_2,y_2,l_2,w_2,ang_2)

    inter = False
    for k,l in zip([0,1,2,3],[1,2,3,0]):
        for m,n in zip([0,1,2,3],[1,2,3,0]):

            x1 = corner_rect_1[k][0]
            y1 = corner_rect_1[k][1]

            x2 = corner_rect_1[l][0]
            y2 = corner_rect_1[l][1]

            x3 = corner_rect_2[m][0]
            y3 = corner_rect_2[m][1]

            x4 = corner_rect_2[n][0]
            y4 = corner_rect_2[n][1]

            intersection = segments_intersection(x1,y1,x2,y2,x3,y3,x4,y4)

            if intersection == True:
                inter = True

    return inter


def conflict(pair):
    '''
    Check conflicts between magnets and pick-up zone of adjacent magnets

    :param pair:
    :return:
    '''

    # Dimensions of interest
    r_circ        = 6.0                             # radius of the circular magnets
    w_rect        = 12.0                            # width of the rectangular magnets
    l_rect        = 20.0                            # length of the rectangular magnets
    g             = 23.0                            # distance between the circular and the rectangular magnets
    L             = (r_circ + g + l_rect / 2.0)     # length between center of the circ. magnet and center of rect. magnet
    l_robot       = 14.02                           # length of the robot pick-up arm
    w_robot       = 5                               # width of the robot pick-up arm
    l_pickup_circ = l_robot                         # the length of the pickup area for the circular magnet
    w_pickup_circ = (3.0 * w_robot / 2.0) + r_circ  # the width of the pickup rea for the circular magnet
    l_pickup_rect = l_robot                         # the length of the pick up area for the rectangle magnet
    w_pickup_rect = 0.5 * (l_rect + 3.0 * w_robot)  # the width of the pickup area for the rectangle magnet
    HECTOR_plate  = calculate_circle_xy_coordinates(0.0, 0.0, 260.0)


    #pair = np.array([[-40.00932124, 100.54825307, 111.69818555,   0., 5.],
    #                 [-21.01479494, 105.05614718, -30.2331867 ,   0.,16.]])


    #plot_plate(HECTOR_plate)

    blocked  = []
    blocking = []
    zone     = []

    shape   = pair[:,3]

    # circle - circle
    if sum(shape) == 0:

        for h,i in zip([0,1],[1,0]):

            plt.figure()

            pickupArea = pickupArea_circ(w_robot, r_circ, pair[h])

            x_c = pair[i][0]
            y_c = pair[i][1]

            # Iterate over the pickup areas (circle magnet has 4 pickup area possible)
            for j in range(len(pickupArea)):
                x_r   = pickupArea[j][0]
                y_r   = pickupArea[j][1]
                ang_r = pickupArea[j][2]

                inter = circle_rect_intersection(x_r,y_r,ang_r,l_pickup_circ,w_pickup_circ,x_c,y_c,r_circ)

                if inter == True:
                    print('Magnet ',pair[h][4],' (pickup zone: ',j,') blocked by magnet ',pair[i][4])
                    blocked.append(pair[h])
                    blocking.append(pair[i])
                    zone.append(j)

    # circle - rectangle
    elif sum(shape) == 1:

        for h, i in zip([0, 1], [1, 0]):

            plt.figure()
            if pair[h][3] == 0:

                pickupArea = pickupArea_circ(w_robot, r_circ, pair[h])
                #drawPickupArea_circ(pickupArea, l_robot, w_robot, r_circ)

                x_c = pair[h][0]
                y_c = pair[h][1]

                # Iterate over the pickup areas (circle magnet has 4 pickup area possible)
                for j in range(len(pickupArea)):

                    x_1   = pickupArea[j][0]
                    y_1   = pickupArea[j][1]
                    ang_1 = pickupArea[j][2]
                    l_1   = l_pickup_circ
                    w_1   = w_pickup_circ
                    x_2   = pair[i][0]
                    y_2   = pair[i][1]
                    ang_2 = pair[i][2] - 90
                    l_2   = l_rect
                    w_2   = w_rect

                    #drawRect(x_2, y_2, w_rect, l_rect, ang_2, 'r')

                    inter = rect_rect_intersection(x_1,y_1,ang_1,l_1,w_1,x_2,y_2,ang_2 ,l_2,w_2)

                    if inter == True:
                        print('Magnet ', pair[h][4],' (pickup zone:',j,') blocked by magnet ', pair[i][4])
                        blocked.append(pair[h])
                        blocking.append(pair[i])
                        zone.append(j)

            elif pair[h][3] == 1:

                pickupArea = pickupArea_rec(w_robot,l_robot,l_rect, pair[h])

                x_c = pair[i][0]
                y_c = pair[i][1]

                # Iterate over the pickup areas (circle magnet has 4 pickup area possible)
                for j in range(len(pickupArea)):

                    x_r   = pickupArea[j][0]
                    y_r   = pickupArea[j][1]
                    ang_r = pickupArea[j][2]

                    inter = circle_rect_intersection(x_r,y_r,ang_r,l_pickup_rect,w_pickup_rect,x_c,y_c,r_circ)

                    if inter == True:
                        print('Magnet ', pair[h][4],' (pickup zone:',j,') blocked by magnet ', pair[i][4])
                        blocked.append(pair[h])
                        blocking.append(pair[i])
                        zone.append(j)


    # rectangle - rectangle
    elif sum(shape) == 2:
        for h, i in zip([0, 1], [1, 0]):

            plt.figure()

            pickupArea = pickupArea_rec(w_robot, l_robot, l_rect, pair[h])

            for j in range(len(pickupArea)):

                x_1   = pickupArea[j][0]
                y_1   = pickupArea[j][1]
                ang_1 = pickupArea[j][2]
                l_1   = l_pickup_rect
                w_1   = w_pickup_rect

                x_2   = pair[i][0]
                y_2   = pair[i][1]
                ang_2 = pair[i][2] - 90
                l_2   = l_rect
                w_2   = w_rect

                inter = rect_rect_intersection(x_1, y_1, ang_1, l_1, w_1, x_2, y_2, ang_2, l_2, w_2)

                if inter == True:
                    print('Magnet ', pair[h][4],' (pickup zone:',j,') blocked by magnet ', pair[i][4])
                    blocked.append(pair[h])
                    blocking.append(pair[i])
                    zone.append(j)

    return blocked,blocking,zone