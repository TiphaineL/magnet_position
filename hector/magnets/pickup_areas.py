from hector.constants import rectangle_magnet_length, robot_arm_width,robot_arm_length,circular_magnet_radius
from operations.shapes.rectangle import rectangle

class rectangular_magnet_pickup_area(rectangle):

    def __init__(self,center,orientation):
        length = 0.5 * (rectangle_magnet_length + 3* robot_arm_width)
        width  = robot_arm_length
        super().__init__(center,length,width,orientation)

class circular_magnet_pickup_area(rectangle):

    def __init__(self,center,orientation):
        length = (3.0/2) * robot_arm_width + circular_magnet_radius
        width  = robot_arm_length
        super().__init__(center,length,width,orientation)

class inward(rectangular_magnet_pickup_area):
    kind = 'inward (toward circular magnet) pickup area'
    pass

class outward(rectangular_magnet_pickup_area):
    kind = 'outward (toward circular magnet) pickup area'
    pass

class tangential_right(circular_magnet_pickup_area):
    kind = 'tangential from right pickup area'
    pass

class tangential_left(circular_magnet_pickup_area):
    kind = 'tangential from left pickup area'
    pass

class radial_inward(circular_magnet_pickup_area):
    kind = 'inward radial pickup area'
    pass

class radial_outward(circular_magnet_pickup_area):
    kind = 'outward radial pickup area'
    pass



