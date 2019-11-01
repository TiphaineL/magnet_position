def plot_plate_with_magnets(r_circ,w_rect,l_rect,HECTOR_plate,mag_c,mag_r):
    # plots HECTOR plate together with the magnets
    # with r_circ the radius of the circular magnets, w_rect and l_rect the width and length of the rectangular magnets
    # respectively, HECTOR_plate the plate, mag_c and mag_r the coordinates of the circular and rectangular magnets
    # respectively (x,y and orientation angle)

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

    i = 0
    for magnet in mag_c:

        # Plot the circular magnets
        x_c = mag_c[i][0]
        y_c = mag_c[i][1]

        magnet_circ = circle(x_c, y_c, r_circ)

        plt.plot(magnet_circ[0], magnet_circ[1], 'r')
        plt.plot(magnet_circ[0], magnet_circ[2], 'r')

        # Plot the rectangular magnet
        x_r   = mag_r[i][0]
        y_r   = mag_r[i][1]
        ang_r = mag_r[i][2]

        drawRect(x_r, y_r, w_rect, l_rect, ang_r, 'r')

        i += 1

    plt.axis('scaled')
    plt.axis([-270, 270, -270, 270])
    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.show()