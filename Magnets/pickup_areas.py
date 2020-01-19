from constants import rectangle_magnet_length, robot_arm_width,robot_arm_length,circular_magnet_radius
from Shapes.rectangle import rectangle

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

