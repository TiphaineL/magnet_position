from shapes import rectangle

class robot_arm(rectangle):

    def __init__(self):
        length = robot_arm_length
        width  = robot_arm_width
        super().__init__(center,length,width,orientation)

class circular_magnet_pickup_area(rectangle):

    def __init__(self):
        super().__init__(center,length,width,orientation)

class rectangular_magnet_pickup_area:

    def __init__(self):
        super().__init__(center,length,width,orientation)