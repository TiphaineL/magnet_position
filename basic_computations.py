import numpy as np
import math
from math import cos, sin
import matplotlib.pyplot as plt


def calculate_circle_xy_coordinates(center_x, center_y, radius):

    x_coordinates = np.arange(center_x - radius, center_x + radius, radius / 100000)

    y_coordinates_negative = -np.sqrt(np.abs(radius ** 2 - (x_coordinates - center_x) ** 2)) + center_y
    y_coordinates_positive = np.sqrt(np.abs(radius ** 2 - (x_coordinates - center_x) ** 2)) + center_y

    return(x_coordinates,y_coordinates_negative,y_coordinates_positive)

def convert_degrees_to_radians(angle_degrees):
    return angle_degrees * np.pi /180

def convert_modulus_angle(angle):
    piX2 = 2 * np.pi

    if angle < piX2:
        angle = angle + piX2
    if angle > piX2:
        angle = angle - piX2
    if angle < 0:
        angle = piX2 - abs(angle)
    return angle

def calculate_rectangle_center_xy_coordinates(center_x, center_y, rectangle_length, orientation):
    '''
    returns the coordinates of the center of the rect magnet
    with x1,y1 the coordinates of the center of the circular magnet, L the length between the circ. and rect. magnets,
    and alpha the absolute angle of the rect. magnet (angle from the x-axis)
    '''

    rectangle_orientation_in_radians = convert_degrees_to_radians(orientation)

    rectangle_orientation = convert_modulus_angle(rectangle_orientation_in_radians)

    # Calculate the center position of the center of the rect. magnets rectangle_center_x rectangle_center_y
    if 0 < rectangle_orientation < np.pi/2:
        rectangle_center_x = center_x + rectangle_length * math.cos(rectangle_orientation)
        rectangle_center_y = center_y + rectangle_length * math.sin(rectangle_orientation)
    if np.pi/2 < rectangle_orientation < np.pi:
        rectangle_center_x = center_x - rectangle_length * math.cos(np.pi - rectangle_orientation)
        rectangle_center_y = center_y + rectangle_length * math.sin(np.pi - rectangle_orientation)
    if np.pi < rectangle_orientation < 3*np.pi/2:
        rectangle_center_x = center_x - rectangle_length * math.sin(3 * np.pi / 2 - rectangle_orientation)
        rectangle_center_y = center_y - rectangle_length * math.cos(3 * np.pi / 2 - rectangle_orientation)
    if 3*np.pi/2 < rectangle_orientation < 2*np.pi:
        rectangle_center_x = center_x + rectangle_length * math.cos(2 * np.pi - rectangle_orientation)
        rectangle_center_y = center_y - rectangle_length * math.sin(2 * np.pi - rectangle_orientation)

    return rectangle_center_x,rectangle_center_y


def drawRect(x0, y0, w, h, angle, col):
    '''
    plots a rectangle
    with x0,y0 the coordinates of the center, w the width, h the height, angle the angle of orientation
    (angle relative to the vertical axis), col the colour to use for plotting
    '''

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


def rectangle_corner(x0,y0,width,height,theta):
    '''
    Returns the coordinates of the 4 corners of a rectangle

    with x0,y0 the coordinates of the center of the rectangle, width and height the width and height of the rectangle,
    theta the angle of rotation of the rectangle relative to the vertical axis (?)
    '''

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


    #for i in range(len(omega)):
    #    plt.plot(corner[0, 0], corner[0, 1], 'xb')
    #    plt.plot(corner[1, 0], corner[1, 1], 'xc')
    #    plt.plot(corner[2, 0], corner[2, 1], 'xg')
    #    plt.plot(corner[3, 0], corner[3, 1], 'xy')
    #    plt.axis('scaled')
    #    plt.show()

    return corner