def circle(x0,y0,r):
    # returns the equation for plotting a circle
    # with x0,y0 the coordinates of the center, r the radius

    import numpy as np

    x = np.arange(x0-r,x0+r,r/100000)

    y_neg = -np.sqrt(np.abs(r**2 - (x-x0)**2)) + y0
    y_pos =  np.sqrt(np.abs(r**2 - (x-x0)**2)) + y0
    return(x,y_neg,y_pos)
