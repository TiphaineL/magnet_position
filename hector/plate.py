import matplotlib.pyplot as plt
from operations.shapes.circle import circle
from hector.constants import HECTOR_plate_center_coordinate,HECTOR_plate_radius

class HECTOR_plate(circle):

    def __init__(self):
        self.center = HECTOR_plate_center_coordinate
        self.radius = HECTOR_plate_radius
        self.orientation = 0

def plot_plate(HECTOR_plate):

    plt.figure()

    plt.plot(HECTOR_plate[0], HECTOR_plate[1], 'r')
    plt.plot(HECTOR_plate[0], HECTOR_plate[2], 'r')
    #plt.plot(0, 0, 'x')

    plt.axis('scaled')
    plt.axis([-270, 270, -270, 270])
    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.show()