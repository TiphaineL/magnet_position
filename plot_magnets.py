def plot_magnets(r_circ,w_rect,l_rect,mag,c):
    # plots the magnets
    # with r_circ the radius of the circular magnets, w_rect and l_rect the width and length of the rectangular magnets
    # respectively, mag the coordinates of the magnets
    # respectively (x,y and orientation angle, 0: circ or 1:rect), c the colour

    import matplotlib.pyplot as plt
    from circle import circle
    from rectangle import drawRect

    i = 0
    for magnet in mag:

        if magnet[3] == 0:
            # Plot the circular magnets
            x_c = mag[i][0]
            y_c = mag[i][1]

            magnet_circ = circle(x_c, y_c, r_circ)

            plt.plot(magnet_circ[0], magnet_circ[1], c)
            plt.plot(magnet_circ[0], magnet_circ[2], c)

        if magnet[3] == 1:
            # Plot the rectangular magnet
            x_r   = mag[i][0]
            y_r   = mag[i][1]
            ang_r = mag[i][2]

            drawRect(x_r, y_r, w_rect, l_rect, ang_r, c)

        i += 1