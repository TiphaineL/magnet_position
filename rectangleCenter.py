def rect_center(x1,y1,L,alpha):
    # returns the coordinates of the center of the rect magnet
    # with x1,y1 the coordinates of the center of the circular magnet, L the length between the circ. and rect. magnets,
    # and alpha the absolute angle of the rect. magnet (angle from the x-axis)

    import math
    import numpy as np

    # convert angle to radians
    alpha = alpha * np.pi / 180

    # Convert angle to remove the modulus 2 pi ( negative )
    if alpha < 2 * np.pi:
        alpha = alpha + 2 * np.pi
    # Convert angle to remove the modulus 2 pi ( positive )
    if alpha > 2 * np.pi:
        alpha = alpha - 2 * np.pi
    # Convert negative angles into positive ( modulus 2 pi )
    if alpha < 0:
        alpha = 2 * np.pi - abs(alpha)

    # Calculate the center position of the center of the rect. magnets x2 y2
    if 0 < alpha < np.pi/2:
        x2 = x1 + L * math.cos(alpha)
        y2 = y1 + L * math.sin(alpha)
    if np.pi/2 < alpha < np.pi:
        x2 = x1 - L * math.cos(np.pi - alpha)
        y2 = y1 + L * math.sin(np.pi - alpha)
    if np.pi < alpha < 3*np.pi/2:
        x2 = x1 - L * math.sin(3*np.pi/2 - alpha)
        y2 = y1 - L * math.cos(3*np.pi/2 - alpha)
    if 3*np.pi/2 < alpha < 2*np.pi:
        x2 = x1 + L * math.cos(2*np.pi - alpha)
        y2 = y1 - L * math.sin(2*np.pi - alpha)

    return x2,y2