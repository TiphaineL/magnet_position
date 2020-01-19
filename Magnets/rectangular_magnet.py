from Shapes.rectangle import rectangle
from constants import rectangle_magnet_length,rectangle_magnet_width,robot_arm_width
from math import sin, cos, pi
from Magnets.pickup_areas import rectangular_magnet_pickup_area
from Operations.trigonometry import convert_degrees_to_radians

class rectangular_magnet(rectangle):

    number_of_rectangular_magnets = 0

    def __init__(self,center,orientation):
        length = rectangle_magnet_length
        width  = rectangle_magnet_width
        super().__init__(center,length,width,orientation)

        rectangular_magnet.number_of_rectangular_magnets += 1

    def calculate_center_magnet_to_center_pickup_area_length():

        center_magnet_to_center_pickup_area_length = 0.25 * (rectangle_magnet_length + robot_arm_width)

        return center_magnet_to_center_pickup_area_length

    def calculate_center_coordinate_outward_pickuparea(self):

        center_coordinates = \
        [self.center[0] + \
         rectangular_magnet.calculate_center_magnet_to_center_pickup_area_length() * sin((pi / 180.0) * (self.orientation)),
         self.center[1] + \
         rectangular_magnet.calculate_center_magnet_to_center_pickup_area_length() * cos((pi / 180.0) * (self.orientation))]

        return center_coordinates

    def calculate_center_coordinate_inward_pickuparea(self):

        center_coordinates = \
        [self.center[0] - \
         rectangular_magnet.calculate_center_magnet_to_center_pickup_area_length() * sin((pi / 180.0) * (self.orientation)),
         self.center[1] - \
         rectangular_magnet.calculate_center_magnet_to_center_pickup_area_length() * cos((pi / 180.0) * (self.orientation))]

        return center_coordinates

    def calculate_pickup_areas(self):

        self.pickup_areas = \
        [rectangular_magnet_pickup_area(rectangular_magnet.calculate_center_coordinate_inward_pickuparea(self), self.orientation),
         rectangular_magnet_pickup_area(rectangular_magnet.calculate_center_coordinate_outward_pickuparea(self),self.orientation)]

        return self.pickup_areas
