from hector.constants import circular_rectangle_magnet_center_distance
from math import pi, cos, sin, atan
import numpy as np
from general_operations.trigonometry import convert_radians_to_degrees, convert_modulus_angle, convert_degrees_to_radians
from hector.magnets.circular import circular_magnet
from hector.magnets.rectangular import rectangular_magnet

class probe:

    def __init__(self, probe_index, circular_magnet_center, rectangular_magnet_input_orientation):

        self.index = probe_index
        self.circular_magnet_center = np.array(circular_magnet_center) * 260.0
        self.rectangular_magnet_input_orientation = rectangular_magnet_input_orientation
        self.circular_rectangle_magnet_center_distance = circular_rectangle_magnet_center_distance

    def calculate_circular_magnet_orientation(self):

        if self.circular_magnet_center[0] > 0 and self.circular_magnet_center[1] > 0:

            self.circular_magnet_orientation = \
            atan(np.abs(self.circular_magnet_center[1] / self.circular_magnet_center[0]))

        elif self.circular_magnet_center[0] < 0 and self.circular_magnet_center[1] > 0:

            self.circular_magnet_orientation = pi - \
            atan(np.abs(self.circular_magnet_center[1] / self.circular_magnet_center[0]))

        elif self.circular_magnet_center[0] < 0 and self.circular_magnet_center[1] < 0:

            self.circular_magnet_orientation = \
            pi + atan(np.abs(self.circular_magnet_center[1] / self.circular_magnet_center[0]))

        elif self.circular_magnet_center[0] > 0 and self.circular_magnet_center[1] < 0:

            self.circular_magnet_orientation = \
            2 * pi - atan(np.abs(self.circular_magnet_center[1] / self.circular_magnet_center[0]))

        self.circular_magnet_orientation = convert_radians_to_degrees(self.circular_magnet_orientation)

        return self.circular_magnet_orientation

    def calculate_rectangular_magnet_orientation(self):

       probe.calculate_circular_magnet_orientation(self)

       self.rectangular_magnet_absolute_orientation_degree = \
       90 - self.circular_magnet_orientation - convert_radians_to_degrees(self.rectangular_magnet_input_orientation)

       return self.rectangular_magnet_absolute_orientation_degree

    def calculate_rectangular_magnet_center_coordinates(self):

        probe.calculate_rectangular_magnet_orientation(self)

        self.rectangular_magnet_orientation_modulo_radians = \
        convert_modulus_angle(convert_degrees_to_radians(90 - self.rectangular_magnet_absolute_orientation_degree))

        if 0 < self.rectangular_magnet_orientation_modulo_radians < pi / 2:

            self.rectangular_magnet_center = \
            [self.circular_magnet_center[0] \
             + self.circular_rectangle_magnet_center_distance * cos(self.rectangular_magnet_orientation_modulo_radians),
             self.circular_magnet_center[1] \
             + self.circular_rectangle_magnet_center_distance * sin(self.rectangular_magnet_orientation_modulo_radians)]

        elif pi / 2 < self.rectangular_magnet_orientation_modulo_radians < pi:

            self.rectangular_magnet_center = \
            [self.circular_magnet_center[0] \
             - self.circular_rectangle_magnet_center_distance * cos(pi - self.rectangular_magnet_orientation_modulo_radians),
             self.circular_magnet_center[1] \
             + self.circular_rectangle_magnet_center_distance * sin(pi - self.rectangular_magnet_orientation_modulo_radians)]

        elif pi < self.rectangular_magnet_orientation_modulo_radians < 3 * pi / 2:

            self.rectangular_magnet_center = \
            [self.circular_magnet_center[0] \
             - self.circular_rectangle_magnet_center_distance * sin(3 * pi / 2 - self.rectangular_magnet_orientation_modulo_radians),
             self.circular_magnet_center[1] \
             - self.circular_rectangle_magnet_center_distance * cos(3 * pi / 2 - self.rectangular_magnet_orientation_modulo_radians)]

        elif 3 * pi / 2 < self.rectangular_magnet_orientation_modulo_radians < 2 * pi:

            self.rectangular_magnet_center = \
            [self.circular_magnet_center[0] \
             + self.circular_rectangle_magnet_center_distance * cos(2 * pi - self.rectangular_magnet_orientation_modulo_radians),
             self.circular_magnet_center[1] \
             - self.circular_rectangle_magnet_center_distance * sin(2 * pi - self.rectangular_magnet_orientation_modulo_radians)]

        return np.array(self.rectangular_magnet_center)

    def extract_circular_magnet_parameters(self):
        return circular_magnet(self.circular_magnet_center, probe.calculate_circular_magnet_orientation(self),self.index)

    def extract_rectangular_magnet_parameters(self):
        return rectangular_magnet(probe.calculate_rectangular_magnet_center_coordinates(self),
                                  probe.calculate_rectangular_magnet_orientation(self),self.index)