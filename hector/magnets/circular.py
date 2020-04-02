from operations.shapes.circle import circle
from hector.constants import circular_magnet_radius,robot_arm_width
from math import sin, cos, pi
from hector.magnets.pickup_areas import tangential_right,tangential_left,radial_inward,radial_outward


class circular_magnet(circle):

    def __init__(self,center,orientation,index):
        radius = circular_magnet_radius
        super().__init__(center,radius,orientation)
        self.index = index
        self.placement_index = 0

    def calculate_center_magnet_to_center_pickup_area_length(self):

        center_magnet_to_center_pickup_area_length = 0.5 * (0.5 * robot_arm_width + self.radius)

        return center_magnet_to_center_pickup_area_length

    def calculate_center_coordinate_tangential_right_pickuparea(self):

        center_coordinates = \
        [self.center[0] + self.calculate_center_magnet_to_center_pickup_area_length() * sin((pi / 180) * (- self.orientation)),
         self.center[1] + self.calculate_center_magnet_to_center_pickup_area_length() * cos((pi / 180) * (- self.orientation))]

        return center_coordinates

    def calculate_center_coordinate_tangential_left_pickuparea(self):

        center_coordinates = \
        [self.center[0] - self.calculate_center_magnet_to_center_pickup_area_length() * sin((pi / 180) * (- self.orientation)),
         self.center[1] - self.calculate_center_magnet_to_center_pickup_area_length() * cos((pi / 180) * (- self.orientation))]

        return center_coordinates

    def calculate_center_coordinates_radial_inward_pickuparea(self):

        center_coordinates = \
        [self.center[0] + self.calculate_center_magnet_to_center_pickup_area_length() * sin((pi / 180) * (90 - self.orientation)),
         self.center[1] + self.calculate_center_magnet_to_center_pickup_area_length() * cos((pi / 180) * (90 - self.orientation))]

        return center_coordinates

    def calculate_center_coordinates_radial_outwards_pickuparea(self):

        center_coordinates = \
        [self.center[0] - self.calculate_center_magnet_to_center_pickup_area_length() * sin((pi / 180) * (90 - self.orientation)),
         self.center[1] - self.calculate_center_magnet_to_center_pickup_area_length() * cos((pi / 180) * (90 - self.orientation))]

        return center_coordinates

    def create_pickup_areas(self):

        self.pickup_areas = \
            [tangential_right(self.calculate_center_coordinate_tangential_right_pickuparea(), -self.orientation),
             tangential_left( self.calculate_center_coordinate_tangential_left_pickuparea(),  -self.orientation),
             radial_inward(   self.calculate_center_coordinates_radial_inward_pickuparea(),   -self.orientation),
             radial_outward(  self.calculate_center_coordinates_radial_outwards_pickuparea(), -self.orientation)]

        return self.pickup_areas

def is_circular_magnet(magnet):
    return isinstance(magnet, circular_magnet)

