def rectangle_corner(x0,y0,width,height,theta):
    # Returns the coordinates of the 4 corners of a rectangle

    # with x0,y0 the coordinates of the center of the rectangle, width and height the width and height of the rectangle,
    # theta the angle of rotation of the rectangle relative to the vertical axis (?)

    import numpy as np
    import math
    from rectangle import drawRect
    import matplotlib.pyplot as plt

    # Calculate the diagonal of the rectangle
    r = 0.5 * np.sqrt( width**2 + height**2 )

    # Calculate the angle of the rectangle diagonal (in the rectangle referencial)
    alpha = math.acos( width/(2*r) ) * (180 / np.pi)

    # Calculate the different angles of the corners (angles relative to the vertical axis)
    omega = np.array( [ theta + alpha ,
                        theta - alpha ,
                        theta + alpha + 180 ,
                        theta - alpha + 180 ] )

    # Calculate the coordinates (x,y) of the corners of the rectangle
    corner = np.array( [x0 + r * np.cos( (np.pi/180) * (180 - omega) ),
                        y0 + r * np.sin( (np.pi/180) * (180 - omega) )] )

    corner = corner.T


    #drawRect(x0,y0,width,height,theta,'r')
    for i in range(len(omega)):
        #print(corner)
        #plt.plot(np.concatenate(corner[:,:,:,0]),np.concatenate(corner[:,:,:,1]),'bx')
        #plt.plot(corner[:, 12, :, 0], corner[:, 12, :, 1], 'bx')
        #plt.plot(corner[:,0],corner[:,1],'xb')
        plt.plot(corner[0, 0], corner[0, 1], 'xb')
        plt.plot(corner[1, 0], corner[1, 1], 'xc')
        plt.plot(corner[2, 0], corner[2, 1], 'xg')
        plt.plot(corner[3, 0], corner[3, 1], 'xy')
        plt.axis('scaled')
        plt.show()

    return corner




