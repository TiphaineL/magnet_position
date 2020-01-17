import numpy as np
from basic_computations import calculate_circle_xy_coordinates,\
                               calculate_rectangle_corners_xy_coordinates
from magnets_functions  import calculate_circular_magnet_pickup_area, \
                               calculate_rectangle_magnet_pickup_area


def circle_segment_intersection(circle_center_x, circle_center_y, segment_start_x, segment_start_y,
                                segment_end_x, segment_end_y, circle_radius):

    segment_vector_x = segment_end_x - segment_start_x
    segment_vector_y = segment_end_y - segment_start_y

    fx = segment_start_x - circle_center_x
    fy = segment_start_y - circle_center_y

    A = segment_vector_x**2 + segment_vector_y**2
    B = 2*( segment_vector_x*fx + segment_vector_y*fy )
    C = fx ** 2 + fy ** 2 - circle_radius ** 2

    Delta = B**2 - 4*A*C

    t1 = (-B + np.sqrt(Delta)) / (2 * A)
    t2 = (-B - np.sqrt(Delta)) / (2 * A)

    x_intersection_1 = segment_start_x + t1 * segment_vector_x

    x_intersection_2 = segment_start_x + t2 * segment_vector_x

    intersection = False

    if Delta >= 0:
        if min(segment_start_x, segment_end_x) <= x_intersection_1 <= max(segment_start_x, segment_end_x):
            intersection = True
        if min(segment_start_x, segment_end_x) <= x_intersection_2 <= max(segment_start_x, segment_end_x):
            intersection = True
    magnet_circ = calculate_circle_xy_coordinates(circle_center_x, circle_center_y, circle_radius)

    #plt.plot([x1,x2],[y1,y2])
    #plt.plot(magnet_circ[0], magnet_circ[1], 'c')
    #plt.plot(magnet_circ[0], magnet_circ[2], 'c')
    #if intersection:
     #   plt.plot(x_intersection_1,y_intersection_1,'xr')
      #  plt.plot(x_intersection_2,y_intersection_2,'xr')
    #plt.axis('scaled')

    return intersection


def circle_rectangle_intersection(rectangle_center_x, rectangle_center_y, rectangle_orientation, rectangle_length,
                                  rectangle_width, circle_center_x, circle_center_y, circle_radius):

    rectangle_corners = calculate_rectangle_corners_xy_coordinates(rectangle_center_x, rectangle_center_y,
                                                            rectangle_length, rectangle_width, rectangle_orientation)


    for k, rectangle_length in zip([0, 1, 2, 3], [1, 2, 3, 0]):

        intersection = circle_segment_intersection(circle_center_x, circle_center_y, rectangle_corners[k][0],
                       rectangle_corners[k][1], rectangle_corners[rectangle_length][0],
                       rectangle_corners[rectangle_length][1], circle_radius)

    return intersection


def segments_intersection(segment1_start_x, segment1_start_y, segment1_end_x, segment1_end_y,
                          segment2_start_x, segment2_start_y, segment2_end_x, segment2_end_y):

    def calculate_line_slope_and_origin(start_x, start_y, end_x, end_y):
        slope = (end_y - start_y) / (end_x - start_x)
        origin = end_y - slope * end_x
        return slope, origin

    intersect = False

    # Check if vertical line (if vertical line: it's not possible to compute the slope)

    if segment1_start_x == segment1_end_x:
        slope,origin = calculate_line_slope_and_origin(segment2_start_x, segment2_start_y, segment2_end_x, segment2_end_y)
        function = slope * segment1_start_x + origin
        if min(segment1_start_y, segment1_end_y) <= function <= max(segment1_start_y, segment1_end_y):
            intersect = True

            intersect_x = segment1_start_x
            intersect_y = function

    elif segment2_start_x == segment2_end_x:
        slope,origin = calculate_line_slope_and_origin(segment1_start_x, segment1_start_y, segment1_end_x, segment1_end_y)
        function = slope * segment2_start_x + origin
        if min(segment2_start_y, segment2_end_y) <= function <= max(segment2_start_y, segment2_end_y):
            intersect = True

            intersect_x = segment2_start_x
            intersect_y = function

    else:
        slope1, origin1 = calculate_line_slope_and_origin(segment1_start_x, segment1_start_y, segment1_end_x, segment1_end_y)
        slope2, origin2 = calculate_line_slope_and_origin(segment2_start_x, segment2_start_y, segment2_end_x, segment2_end_y)


        if slope1 != slope2:

            intersect_x = (origin2 - origin1) / (slope1 - slope2)
            intersect_y = slope1 * intersect_x + origin1

            if min(segment1_start_x, segment1_end_x) <= intersect_x <= max(segment1_start_x, segment1_end_x):
                if min(segment2_start_x, segment2_end_x) <= intersect_x <= max(segment2_start_x, segment2_end_x):
                    intersect = True

    #import matplotlib.pyplot as plt
    #plt.plot([x1, x2], [y1, y2], 'b')
    #plt.plot([x3, x4], [y3, y4], 'b')
    #if intersect:
    #    plt.plot(intersect_x, intersect_y, 'xb')

    return intersect


def rectangle_rectangle_intersection(rectangle1_center_x, rectangle1_center_y, rectangle1_orientation,
                                     rectangle1_length, rectangle1_width, rectangle2_center_x, rectangle2_center_y,
                                     rectangle2_orientation, rectangle2_length, rectangle2_width):

    rectangle1_corners_coordinates = calculate_rectangle_corners_xy_coordinates(rectangle1_center_x,
                                     rectangle1_center_y,rectangle1_length, rectangle1_width, rectangle1_orientation)

    rectangle2_corners_coordinates = calculate_rectangle_corners_xy_coordinates(rectangle2_center_x,
                                     rectangle2_center_y,rectangle2_length, rectangle2_width, rectangle2_orientation)

    inter = False

    for k,l in zip([0,1,2,3],[1,2,3,0]):
        for m,n in zip([0,1,2,3],[1,2,3,0]):

            x1 = rectangle1_corners_coordinates[k][0]
            y1 = rectangle1_corners_coordinates[k][1]

            x2 = rectangle1_corners_coordinates[l][0]
            y2 = rectangle1_corners_coordinates[l][1]

            x3 = rectangle2_corners_coordinates[m][0]
            y3 = rectangle2_corners_coordinates[m][1]

            x4 = rectangle2_corners_coordinates[n][0]
            y4 = rectangle2_corners_coordinates[n][1]

            if segments_intersection(x1,y1,x2,y2,x3,y3,x4,y4):
                inter = True

    return inter

def circle_and_circle_magnets(magnet_pair):
    return sum(magnet_pair[:, 3]) == 0

def circle_rectangle_magnets(magnet_pair):
    return sum(magnet_pair[:, 3]) == 1

def magnet_is_circular(magnet):
    return magnet[3] == 0

def magnet_is_rectangular(magnet):
    return magnet[3] == 1

def conflict(magnet_pair):

    from constants import circular_magnet_radius,rectangle_magnet_width,rectangle_magnet_length,robot_arm_width,\
                          circular_magnet_pickuparea_length,circular_magnet_pickuparea_width,\
                          rectangle_magnet_pickuparea_length,rectangle_magnet_pickuparea_width

    blocked  = []
    blocking = []
    zone     = []

    magnet_shape = magnet_pair[:, 3]

    if circle_and_circle_magnets(magnet_pair):

        for h,i in zip([0,1],[1,0]):

            #plt.figure()

            pickupArea = calculate_circular_magnet_pickup_area(robot_arm_width, circular_magnet_radius, magnet_pair[h])

            circular_magnet_center_x = magnet_pair[i][0]
            circular_magnet_center_y = magnet_pair[i][1]

            # Iterate over the pickup areas (circle magnet has 4 pickup area possible)
            for j in range(len(pickupArea)):
                pickuparea_center_x    = pickupArea[j][0]
                pickuparea_center_y    = pickupArea[j][1]
                pickuparea_orientation = pickupArea[j][2]

                inter = circle_rectangle_intersection(pickuparea_center_x, pickuparea_center_y, pickuparea_orientation,
                               circular_magnet_pickuparea_length, circular_magnet_pickuparea_width, circular_magnet_center_x, circular_magnet_center_y, circular_magnet_radius)

                if inter == True:
                    print('Magnet ', magnet_pair[h][4], ' (pickup zone: ', j, ') blocked by magnet ', magnet_pair[i][4])
                    blocked.append(magnet_pair[h])
                    blocking.append(magnet_pair[i])
                    zone.append(j)


    elif circle_rectangle_magnets(magnet_pair):

        for h, i in zip([0, 1], [1, 0]):

            #plt.figure()
            if magnet_is_circular(magnet_pair[h]):

                pickupArea = calculate_circular_magnet_pickup_area(robot_arm_width, circular_magnet_radius, magnet_pair[h])

                # Iterate over the pickup areas (circle magnet has 4 pickup area possible)
                for j in range(len(pickupArea)):

                    x_1   = pickupArea[j][0]
                    y_1   = pickupArea[j][1]
                    ang_1 = pickupArea[j][2]
                    l_1   = circular_magnet_pickuparea_length
                    w_1   = circular_magnet_pickuparea_width
                    x_2   = magnet_pair[i][0]
                    y_2   = magnet_pair[i][1]
                    ang_2 = magnet_pair[i][2] - 90
                    l_2   = rectangle_magnet_length
                    w_2   = rectangle_magnet_width

                    #drawRect(x_2, y_2, w_rect, l_rect, ang_2, 'r')

                    inter = rectangle_rectangle_intersection(x_1, y_1, ang_1, l_1, w_1, x_2, y_2, ang_2, l_2, w_2)

                    if inter == True:
                        print('Magnet ', magnet_pair[h][4], ' (pickup zone:', j, ') blocked by magnet ', magnet_pair[i][4])
                        blocked.append(magnet_pair[h])
                        blocking.append(magnet_pair[i])
                        zone.append(j)

            elif magnet_pair[h][3] == 1:

                pickupArea = calculate_rectangle_magnet_pickup_area(robot_arm_width, rectangle_magnet_length, magnet_pair[h])

                circular_magnet_center_x = magnet_pair[i][0]
                circular_magnet_center_y = magnet_pair[i][1]

                # Iterate over the pickup areas (circle magnet has 4 pickup area possible)
                for j in range(len(pickupArea)):

                    pickuparea_center_x   = pickupArea[j][0]
                    pickuparea_center_y   = pickupArea[j][1]
                    pickuparea_orientation = pickupArea[j][2]

                    inter = circle_rectangle_intersection(pickuparea_center_x, pickuparea_center_y, pickuparea_orientation, rectangle_magnet_pickuparea_length, rectangle_magnet_pickuparea_width, circular_magnet_center_x, circular_magnet_center_y, circular_magnet_radius)

                    if inter == True:
                        print('Magnet ', magnet_pair[h][4], ' (pickup zone:', j, ') blocked by magnet ', magnet_pair[i][4])
                        blocked.append(magnet_pair[h])
                        blocking.append(magnet_pair[i])
                        zone.append(j)


    # rectangle - rectangle
    elif sum(magnet_shape) == 2:
        for h, i in zip([0, 1], [1, 0]):

            #plt.figure()

            pickupArea = calculate_rectangle_magnet_pickup_area(robot_arm_width, rectangle_magnet_length, magnet_pair[h])

            for j in range(len(pickupArea)):

                x_1   = pickupArea[j][0]
                y_1   = pickupArea[j][1]
                ang_1 = pickupArea[j][2]
                l_1   = rectangle_magnet_pickuparea_length
                w_1   = rectangle_magnet_pickuparea_width

                x_2   = magnet_pair[i][0]
                y_2   = magnet_pair[i][1]
                ang_2 = magnet_pair[i][2] - 90
                l_2   = rectangle_magnet_length
                w_2   = rectangle_magnet_width

                inter = rectangle_rectangle_intersection(x_1, y_1, ang_1, l_1, w_1, x_2, y_2, ang_2, l_2, w_2)

                if inter == True:
                    print('Magnet ', magnet_pair[h][4], ' (pickup zone:', j, ') blocked by magnet ', magnet_pair[i][4])
                    blocked.append(magnet_pair[h])
                    blocking.append(magnet_pair[i])
                    zone.append(j)

    return blocked,blocking,zone