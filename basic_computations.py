import numpy as np
import math
from math import cos, sin, pi
import matplotlib.pyplot as plt

def rotational_matrix(rotation_angle):
    return [[cos(rotation_angle), - sin(rotation_angle)],
            [sin(rotation_angle),   cos(rotation_angle)]]

def convert_degrees_to_radians(angle_degrees):
    return angle_degrees * pi /180

def convert_modulus_angle(angle):
    piX2 = 2 * pi

    if angle > piX2:
        angle = angle - piX2
    if angle < 0:
        angle = piX2 - abs(angle)

    return angle

def calculate_circle_xy_coordinates(center_x, center_y, radius):

    x_coordinates = np.arange(center_x - radius, center_x + radius, radius / 100000)

    y_coordinates_negative = -np.sqrt(np.abs(radius ** 2 - (x_coordinates - center_x) ** 2)) + center_y
    y_coordinates_positive =  np.sqrt(np.abs(radius ** 2 - (x_coordinates - center_x) ** 2)) + center_y

    return(x_coordinates,y_coordinates_negative,y_coordinates_positive)

def calculate_center_coordinates_rectangular_magnet(center_x, center_y, rectangle_length,rectangle_magnet_orientation):

    if 0 < rectangle_magnet_orientation < pi / 2:
        rectangle_center_x = center_x + rectangle_length * math.cos(rectangle_magnet_orientation)
        rectangle_center_y = center_y + rectangle_length * math.sin(rectangle_magnet_orientation)

    if pi / 2 < rectangle_magnet_orientation < pi:
        rectangle_center_x = center_x - rectangle_length * math.cos(pi - rectangle_magnet_orientation)
        rectangle_center_y = center_y + rectangle_length * math.sin(pi - rectangle_magnet_orientation)

    if pi < rectangle_magnet_orientation < 3 * pi / 2:
        rectangle_center_x = center_x - rectangle_length * math.sin(3 * pi / 2 - rectangle_magnet_orientation)
        rectangle_center_y = center_y - rectangle_length * math.cos(3 * pi / 2 - rectangle_magnet_orientation)

    if 3 * pi / 2 < rectangle_magnet_orientation < 2 * pi:
        rectangle_center_x = center_x + rectangle_length * math.cos(2 * pi - rectangle_magnet_orientation)
        rectangle_center_y = center_y - rectangle_length * math.sin(2 * pi - rectangle_magnet_orientation)

    return (rectangle_center_x, rectangle_center_y)

def calculate_rectangle_center_xy_coordinates(center_x, center_y, rectangle_length, rectangle_orientation):

    rectangle_orientation_in_radians = convert_degrees_to_radians(rectangle_orientation)

    rectangle_orientation_modulo = convert_modulus_angle(rectangle_orientation_in_radians)

    rectangle_center_xy_coordinates = calculate_center_coordinates_rectangular_magnet(center_x,center_y,\
                                                                    rectangle_length,rectangle_orientation_modulo)

    return rectangle_center_xy_coordinates

def calculate_rectangle_corners_xy_coordinates(rectangle_center_x_coordinate, rectangle_y_coordinate, rectangle_width, rectangle_height,rectangle_orientation):

    x_vector = (cos(rectangle_orientation), -sin(rectangle_orientation))
    y_vector = (sin(rectangle_orientation), cos(rectangle_orientation))

    a = (rectangle_center_x_coordinate - x_vector[0] * rectangle_width / 2 - y_vector[0] * rectangle_height / 2, \
         rectangle_y_coordinate - x_vector[1] * rectangle_width / 2 - y_vector[1] * rectangle_height / 2)

    b = (rectangle_center_x_coordinate + x_vector[0] * rectangle_width / 2 - y_vector[0] * rectangle_height / 2, \
         rectangle_y_coordinate + x_vector[1] * rectangle_width / 2 - y_vector[1] * rectangle_height / 2)

    c = (rectangle_center_x_coordinate + x_vector[0] * rectangle_width / 2 + y_vector[0] * rectangle_height / 2, \
         rectangle_y_coordinate + x_vector[1] * rectangle_width / 2 + y_vector[1] * rectangle_height / 2)

    d = (rectangle_center_x_coordinate - x_vector[0] * rectangle_width / 2 + y_vector[0] * rectangle_height / 2, \
         rectangle_y_coordinate - x_vector[1] * rectangle_width / 2 + y_vector[1] * rectangle_height / 2)

    return [a,b,c,d]

def draw_rectangle(rectangle_center_x_coordinate, rectangle_y_coordinate, rectangle_width, rectangle_height, \
                   rectangle_orientation, plotting_colour):

    rectangle_orientation = np.deg2rad(rectangle_orientation)

    x_vector = (cos(rectangle_orientation), -sin(rectangle_orientation))
    y_vector = (sin(rectangle_orientation),  cos(rectangle_orientation))

    a = (rectangle_center_x_coordinate - x_vector[0] * rectangle_width / 2 - y_vector[0] * rectangle_height / 2, \
         rectangle_y_coordinate - x_vector[1] * rectangle_width / 2 - y_vector[1] * rectangle_height / 2)

    b = (rectangle_center_x_coordinate + x_vector[0] * rectangle_width / 2 - y_vector[0] * rectangle_height / 2, \
         rectangle_y_coordinate + x_vector[1] * rectangle_width / 2 - y_vector[1] * rectangle_height / 2)

    c = (rectangle_center_x_coordinate + x_vector[0] * rectangle_width / 2 + y_vector[0] * rectangle_height / 2, \
         rectangle_y_coordinate + x_vector[1] * rectangle_width / 2 + y_vector[1] * rectangle_height / 2)

    d = (rectangle_center_x_coordinate - x_vector[0] * rectangle_width / 2 + y_vector[0] * rectangle_height / 2, \
         rectangle_y_coordinate - x_vector[1] * rectangle_width / 2 + y_vector[1] * rectangle_height / 2)

    plt.plot([ a[0], b[0] ], [ a[1], b[1] ], plotting_colour)
    plt.plot([ b[0], c[0] ], [ b[1], c[1] ], plotting_colour)
    plt.plot([ c[0], d[0] ], [ c[1], d[1] ], plotting_colour)
    plt.plot([ d[0], a[0] ], [ d[1], a[1] ], plotting_colour)

    return a,b,c,d