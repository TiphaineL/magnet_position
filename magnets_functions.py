from basic_computations import draw_rectangle, calculate_rectangle_center_xy_coordinates, calculate_circle_xy_coordinates
import numpy as np
import math
import matplotlib.pyplot as plt

def draw_circular_magnet_pickup_area(pickuparea_coordinates, robot_arm_length, robot_arm_width, circular_magnet_radius):

    draw_rectangle(pickuparea_coordinates[0][0], pickuparea_coordinates[0][1], robot_arm_length,
                   (3.0 * robot_arm_width / 2.0) + circular_magnet_radius, pickuparea_coordinates[0][2], 'y')
    draw_rectangle(pickuparea_coordinates[1][0], pickuparea_coordinates[1][1], robot_arm_length,
                   (3.0 * robot_arm_width / 2.0) + circular_magnet_radius, pickuparea_coordinates[1][2], 'y')
    draw_rectangle(pickuparea_coordinates[2][0], pickuparea_coordinates[2][1], robot_arm_length,
                   (3.0 * robot_arm_width / 2.0) + circular_magnet_radius, pickuparea_coordinates[2][2], 'y')
    draw_rectangle(pickuparea_coordinates[3][0], pickuparea_coordinates[3][1], robot_arm_length,
                   (3.0 * robot_arm_width / 2.0) + circular_magnet_radius, pickuparea_coordinates[3][2], 'y')


def draw_rectangular_magnet_pickup_area(pickuparea_coordinates, robot_arm_length, robot_arm_width, rectangle_magnet_length):

    draw_rectangle(pickuparea_coordinates[0][0], pickuparea_coordinates[0][1], robot_arm_length,
                   0.5 * (rectangle_magnet_length + 3.0 * robot_arm_width), pickuparea_coordinates[0][2], 'c')
    draw_rectangle(pickuparea_coordinates[1][0], pickuparea_coordinates[1][1], robot_arm_length,
                   0.5 * (rectangle_magnet_length + 3.0 * robot_arm_width), pickuparea_coordinates[1][2], 'c')

def draw_robot_arm(magnet_list, robot_arm_width, robot_arm_length):

    i = 0
    for magnet in magnet_list:

        if circular_magnet(magnet):

            draw_rectangle(magnet_list[i][0], magnet_list[i][1], robot_arm_width,robot_arm_length, - magnet_list[i][2], 'g')
            draw_rectangle(magnet_list[i][0], magnet_list[i][1], robot_arm_width,robot_arm_length, - magnet_list[i][2] + 90, 'g')

        if rectangle_magnet(magnet):

            draw_rectangle(magnet_list[i][0], magnet_list[i][1], robot_arm_width, robot_arm_length,  magnet_list[i][2] + 90, 'g')

        i += 1


def extract_magnets_positions(probe, circular_magnet_center_coordinate_x, circular_magnet_center_y_coordinate,
                              rectangle_magnet_orientation, circular_rectangle_magnet_center_distance):

    circular_magnets    = []
    rectangular_magnets = []

    for magnet in probe:

        circular_magnet_center_x = circular_magnet_center_coordinate_x[int(magnet) - 1] * 260.0
        circular_magnet_center_y = circular_magnet_center_y_coordinate[int(magnet) - 1] * 260.0

        if circular_magnet_center_x > 0 and circular_magnet_center_y > 0:
            circular_magnet_rotational_angle = math.atan(np.abs(circular_magnet_center_y / circular_magnet_center_x))

        elif circular_magnet_center_x < 0 and circular_magnet_center_y > 0:
            circular_magnet_rotational_angle = np.pi - math.atan(np.abs(circular_magnet_center_y / circular_magnet_center_x))

        elif circular_magnet_center_x < 0 and circular_magnet_center_y < 0:
            circular_magnet_rotational_angle = np.pi + math.atan(np.abs(circular_magnet_center_y / circular_magnet_center_x))

        elif circular_magnet_center_x > 0 and circular_magnet_center_y < 0:
            circular_magnet_rotational_angle = 2 * np.pi - math.atan(np.abs(circular_magnet_center_y / circular_magnet_center_x))

        # Convert into degrees
        circular_magnet_rotational_angle = circular_magnet_rotational_angle * (180 / np.pi)

        circular_magnets.append([circular_magnet_center_x, circular_magnet_center_y,circular_magnet_rotational_angle,\
                                 0,probe[int(magnet)-1]])

        # From the file fetch the angle of the rectangular magnet (angle relative to the tangent of the radius -
        # See Olivia's notes for details)
        theta = rectangle_magnet_orientation[int(magnet) - 1] * (180 / np.pi) + 90

        # The angle of the rectangular magnet (absolute)
        alpha = circular_magnet_rotational_angle + theta - 90

        [x_r, y_r] = calculate_rectangle_center_xy_coordinates(circular_magnet_center_x, circular_magnet_center_y, circular_rectangle_magnet_center_distance, alpha)

        ang_r = 90 - alpha

        rectangular_magnets.append([x_r,y_r,ang_r,1,probe[int(magnet)-1]])

    return circular_magnets, rectangular_magnets

def calculate_circular_magnet_pickup_area(robot_arm_width, circular_magnet_radius, magnet):

    # Calculate the hypotenuse of the triangle between the center of the circular magnet to the center fo the pickup_areas
    # and the projected center of the pickup_areas on the vertical axis
    h = 0.5 * (0.5 * robot_arm_width + circular_magnet_radius)

    circular_center_x_coordinate = magnet[0]
    circular_center_y_coordinate = magnet[1]
    circular_magnet_orientation  = magnet[2]

    pickuparea_tangential_right_x_coordinate = \
    circular_center_x_coordinate + h * math.sin((np.pi / 180) * (- circular_magnet_orientation))
    pickuparea_tangential_right_y_coordinate = \
    circular_center_y_coordinate + h * math.cos((np.pi / 180) * (- circular_magnet_orientation))

    pickuparea_tangential_left_x_coordinate = \
    circular_center_x_coordinate - h * math.sin((np.pi / 180) * (- circular_magnet_orientation))
    pickuparea_tangential_left_y_coordinate = \
    circular_center_y_coordinate - h * math.cos((np.pi / 180) * (- circular_magnet_orientation))

    pickuparea_radial_inward_x_coordinate = \
    circular_center_x_coordinate + h * math.sin((np.pi / 180) * (90 - circular_magnet_orientation))
    pickuparea_radial_inward_y_coordinate = \
    circular_center_y_coordinate + h * math.cos((np.pi / 180) * (90 - circular_magnet_orientation))

    pickuparea_radial_outward_x_coordinate = \
    circular_center_x_coordinate - h * math.sin((np.pi / 180) * (90 - circular_magnet_orientation))
    pickuparea_radial_outward_y_coordinate = \
    circular_center_y_coordinate - h * math.cos((np.pi / 180) * (90 - circular_magnet_orientation))

    pickup_areas = \
    [[pickuparea_tangential_right_x_coordinate, pickuparea_tangential_right_y_coordinate, -circular_magnet_orientation],
    [pickuparea_tangential_left_x_coordinate,   pickuparea_tangential_left_y_coordinate,  -circular_magnet_orientation],
    [pickuparea_radial_inward_x_coordinate,     pickuparea_radial_inward_y_coordinate,    -circular_magnet_orientation],
    [pickuparea_radial_outward_x_coordinate,    pickuparea_radial_outward_y_coordinate,   -circular_magnet_orientation]]

    return pickup_areas

def calculate_center_coordinate_outward_pickuparea_rectangle_magnet(rectangle_center_x_coordinate,
                                                        rectangle_center_y_coordinate,h,rectangle_orientation):

    center_x_coordinate = rectangle_center_x_coordinate + h * math.sin((np.pi / 180.0) * (rectangle_orientation))
    center_y_coordinate = rectangle_center_y_coordinate + h * math.cos((np.pi / 180.0) * (rectangle_orientation))

    return center_x_coordinate,center_y_coordinate

def calculate_center_coordinate_inward_pickuparea_rectangle_magnet(rectangle_center_x_coordinate,
                                                                rectangle_center_y_coordinate,h,rectangle_orientation):

    center_x_coordinate = rectangle_center_x_coordinate - h * math.sin((np.pi / 180.0) * (rectangle_orientation))
    center_y_coordinate = rectangle_center_y_coordinate - h * math.cos((np.pi / 180.0) * (rectangle_orientation))

    return center_x_coordinate,center_y_coordinate

def calculate_rectangle_magnet_pickup_area(robot_arm_width, rectangle_magnet_length, magnet):

    # Calculate the hypotenuse of the triangle between the center of the rectangular magnet to the center of the area
    # and the projected center of the area on the vertical axis - See Tiph's notes
    h = 0.25 * (rectangle_magnet_length + robot_arm_width)

    rectangle_center_x_coordinate = magnet[0]
    rectangle_center_y_coordinate = magnet[1]
    rectangle_orientation         = magnet[2]

    outward_pickup_area_rectangle_magnet = calculate_center_coordinate_outward_pickuparea_rectangle_magnet(
        rectangle_center_x_coordinate,rectangle_center_y_coordinate,h,rectangle_orientation)

    inward_pickup_area_rectangle_magnet = calculate_center_coordinate_inward_pickuparea_rectangle_magnet(
        rectangle_center_x_coordinate,rectangle_center_y_coordinate,h,rectangle_orientation)

    area = [ [outward_pickup_area_rectangle_magnet[0], outward_pickup_area_rectangle_magnet[1], rectangle_orientation],
             [inward_pickup_area_rectangle_magnet[0],  inward_pickup_area_rectangle_magnet[1],  rectangle_orientation]]

    return area

def circular_magnet(magnet):

    return magnet[3] == 0

def rectangle_magnet(magnet):

    return magnet[3] == 1

def plot_magnets(circular_magnet_radius, rectangle_magnet_width, rectangle_magnet_length, magnets_list, plotting_colour):

    i = 0
    for magnet in magnets_list:

        if circular_magnet(magnet):

            magnet_center_x_coordinate = magnets_list[i][0]
            magnet_center_y_coordinate = magnets_list[i][1]

            circular_magnet_coordinates = calculate_circle_xy_coordinates(magnet_center_x_coordinate,
                                                                    magnet_center_y_coordinate, circular_magnet_radius)

            plt.plot(circular_magnet_coordinates[0], circular_magnet_coordinates[1], plotting_colour)
            plt.plot(circular_magnet_coordinates[0], circular_magnet_coordinates[2], plotting_colour)
            plt.text(magnet_center_x_coordinate, magnet_center_y_coordinate, str(i+1), fontsize=6)

        if rectangle_magnet(magnet):

            rectangle_center_x_coordinate = magnets_list[i][0]
            rectangle_center_y_coordinate = magnets_list[i][1]
            rectangle_orientation = magnets_list[i][2]

            draw_rectangle(rectangle_center_x_coordinate, rectangle_center_y_coordinate, rectangle_magnet_width,
                           rectangle_magnet_length, rectangle_orientation, plotting_colour)


        i += 1


def plot_plate(HECTOR_plate):

    plt.figure()

    plt.plot(HECTOR_plate[0], HECTOR_plate[1], 'r')
    plt.plot(HECTOR_plate[0], HECTOR_plate[2], 'r')
    #plt.plot(0, 0, 'x')

    plt.axis('scaled')
    plt.axis([-270, 270, -270, 270])
    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.show()