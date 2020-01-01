def conflict(pair):
### Check conflicts between magnets and pick-up zone of adjacent magnets (that have previously been f;agged in proximit

    import numpy as np
    from pickupArea_circ import pickupArea_circ
    from draw_pickupArea_circ import drawPickupArea_circ
    from pickupArea_rec import pickupArea_rec
    from draw_pickupArea_rect import drawPickupArea_rect
    from rect_corner import rectangle_corner
    import matplotlib.pyplot as plt
    from circle import circle
    from plot_plate import plot_plate
    from circle_rectangle_intersection import circle_rect_intersection
    from rectangle_rectangle_intersection import rect_rect_intersection
    from rectangle import drawRect


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
    HECTOR_plate  = circle(0.0,0.0,260.0)


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








