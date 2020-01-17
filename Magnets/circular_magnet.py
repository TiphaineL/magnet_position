from Shapes.circle import circle
from constants import circular_magnet_radius

class circular_magnet(circle):

    number_of_circular_magnets = 0

    def __init__(self,center,orientation):
        radius = circular_magnet_radius
        super().__init__(center,radius,orientation)

        circular_magnet.number_of_circular_magnets += 1