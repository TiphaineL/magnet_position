from Shapes.circle import circle
from constants import circular_magnet_radius,robot_arm_width
from math import sin, cos, pi
from Magnets.pickup_areas import circular_magnet_pickup_area

class circular_magnet(circle):

    number_of_circular_magnets = 0

    def __init__(self,center,orientation):
        radius = circular_magnet_radius
        super().__init__(center,radius,orientation)

        circular_magnet.number_of_circular_magnets += 1

    def calculate_center_magnet_to_center_pickup_area_length(self):

        center_magnet_to_center_pickup_area_length = 0.5 * (0.5 * robot_arm_width + self.radius)

        return center_magnet_to_center_pickup_area_length

    def calculate_center_coordinate_tangential_right_pickuparea(self):

        center_coordinates = \
        [self.center[0] + circular_magnet.calculate_center_magnet_to_center_pickup_area_length(self) * sin((pi / 180) * (- self.orientation)),
         self.center[1] + circular_magnet.calculate_center_magnet_to_center_pickup_area_length(self) * cos((pi / 180) * (- self.orientation))]

        return center_coordinates

    def calculate_center_coordinate_tangential_left_pickuparea(self):

        center_coordinates = \
        [self.center[0] - circular_magnet.calculate_center_magnet_to_center_pickup_area_length(self) * sin((pi / 180) * (- self.orientation)),
         self.center[1] - circular_magnet.calculate_center_magnet_to_center_pickup_area_length(self) * cos((pi / 180) * (- self.orientation))]

        return center_coordinates

    def calculate_center_coordinates_radial_inward_pickuparea(self):

        center_coordinates = \
        [self.center[0] + circular_magnet.calculate_center_magnet_to_center_pickup_area_length(self) * sin((pi / 180) * (90 - self.orientation)),
         self.center[1] + circular_magnet.calculate_center_magnet_to_center_pickup_area_length(self) * cos((pi / 180) * (90 - self.orientation))]

        return center_coordinates

    def calculate_center_coordinates_radial_outwards_pickuparea(self):

        center_coordinates = \
        [self.center[0] - circular_magnet.calculate_center_magnet_to_center_pickup_area_length(self) * sin((pi / 180) * (90 - self.orientation)),
         self.center[1] - circular_magnet.calculate_center_magnet_to_center_pickup_area_length(self) * cos((pi / 180) * (90 - self.orientation))]

        return center_coordinates

    def calculate_pickup_areas(self):

        self.pickup_areas = \
            [circular_magnet_pickup_area(circular_magnet.calculate_center_coordinate_tangential_right_pickuparea(self), -self.orientation),
             circular_magnet_pickup_area(circular_magnet.calculate_center_coordinate_tangential_left_pickuparea(self),  -self.orientation),
             circular_magnet_pickup_area(circular_magnet.calculate_center_coordinates_radial_inward_pickuparea(self),   -self.orientation),
             circular_magnet_pickup_area(circular_magnet.calculate_center_coordinates_radial_outwards_pickuparea(self), -self.orientation)]

        return self.pickup_areas