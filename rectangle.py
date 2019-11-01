def drawRect(x0, y0, w, h, angle, col):
    # plots a rectangle
    # with x0,y0 the coordinates of the center, w the width, h the height, angle the angle of orientation
    # (angle relative to the vertical axis), col the colour to use for plotting


    from math import cos, sin, pi
    import numpy as np
    import matplotlib.pyplot as plt

    angle = np.deg2rad(angle)

    x_vec = (cos(angle), -sin(angle))
    y_vec = (sin(angle),  cos(angle))

    a = (x0 - x_vec[0] * w / 2 - y_vec[0] * h / 2, y0 - x_vec[1] * w / 2 - y_vec[1] * h / 2)

    b = (x0 + x_vec[0] * w / 2 - y_vec[0] * h / 2, y0 + x_vec[1] * w / 2 - y_vec[1] * h / 2)

    c = (x0 + x_vec[0] * w / 2 + y_vec[0] * h / 2, y0 + x_vec[1] * w / 2 + y_vec[1] * h / 2)

    d = (x0 - x_vec[0] * w / 2 + y_vec[0] * h / 2, y0 - x_vec[1] * w / 2 + y_vec[1] * h / 2)

    plt.plot([ a[0], b[0] ], [ a[1], b[1] ], col)
    plt.plot([ b[0], c[0] ], [ b[1], c[1] ], col)
    plt.plot([ c[0], d[0] ], [ c[1], d[1] ], col)
    plt.plot([ d[0], a[0] ], [ d[1], a[1] ], col)

    return a,b,c,d