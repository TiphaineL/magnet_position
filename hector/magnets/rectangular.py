from operations.shapes.rectangle import rectangle
from hector.constants import rectangle_magnet_length,rectangle_magnet_width,robot_arm_width
from math import sin, cos, pi
from hector.magnets.pickup_areas import inward, outward

class rectangular_magnet(rectangle):

    def __init__(self,center,orientation,index):
        length = rectangle_magnet_length
        width  = rectangle_magnet_width
        super().__init__(center,length,width,orientation)
        self.index = index

    def calculate_center_magnet_to_center_pickup_area_length(self):

        center_magnet_to_center_pickup_area_length = 0.25 * (self.length + robot_arm_width)

        return center_magnet_to_center_pickup_area_length

    def calculate_center_coordinate_outward_pickuparea(self):

        center_coordinates = \
        [self.center[0] + self.calculate_center_magnet_to_center_pickup_area_length() * sin((pi / 180.0) * (self.orientation)),
         self.center[1] + self.calculate_center_magnet_to_center_pickup_area_length() * cos((pi / 180.0) * (self.orientation))]

        return center_coordinates

    def calculate_center_coordinate_inward_pickuparea(self):

        center_coordinates = \
        [self.center[0] - self.calculate_center_magnet_to_center_pickup_area_length() * sin((pi / 180.0) * (self.orientation)),
         self.center[1] - self.calculate_center_magnet_to_center_pickup_area_length() * cos((pi / 180.0) * (self.orientation))]

        return center_coordinates

    def create_pickup_areas(self):

        self.pickup_areas = \
        [inward(self.calculate_center_coordinate_inward_pickuparea(), self.orientation),
         outward(self.calculate_center_coordinate_outward_pickuparea(),self.orientation)]

        return self.pickup_areas

def is_rectangular_magnet(magnet):
    return isinstance(magnet, rectangular_magnet)
