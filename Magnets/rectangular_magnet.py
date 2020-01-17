from Shapes.rectangle import rectangle
from constants import rectangle_magnet_length,rectangle_magnet_width

class rectangular_magnet(rectangle):

    number_of_rectangular_magnets = 0

    def __init__(self,center,orientation):
        length = rectangle_magnet_length
        width  = rectangle_magnet_width
        super().__init__(center,length,width,orientation)

        rectangular_magnet.number_of_rectangular_magnets += 1