def extract_positions(probe,x,y,angs_azAng,L):
    # Extract the coordinates of the magnets (x,y, orientation angle)
    # with x, y the coordinates of the circular magnet,  angs_azAngs the angle of the rectangular magnet

    import numpy as np
    from rectangleCenter import rect_center
    import math

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

        mag_c.append([x_c, y_c,angle])

        # From the file fetch the angle of the rectangular magnet (angle relative to the tangent of the radius -
        # See Olivia's notes for details)
        theta = angs_azAng[int(i) - 1] * (180 / np.pi) + 90

        # The angle of the rectangular magnet (absolute)
        alpha = angle + theta - 90

        [x_r, y_r] = rect_center(x_c, y_c, L, alpha)

        ang_r = 90 - alpha

        mag_r.append([x_r,y_r,ang_r])

    return mag_c, mag_r