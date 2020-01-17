import numpy as np
import matplotlib.pyplot as plt

class circle:

    def __init__(self, center,radius,orientation):

        self.center = center
        self.radius = radius
        self.orientation = orientation

    def calculate_circle_all_coordinates(self):

        self.x_coordinates = np.arange(self.center[0] - self.radius, self.center[0] + self.radius, self.radius / 100000)
        self.y_coordinates_negative = -np.sqrt(np.abs(self.radius ** 2 - (self.x_coordinates - self.center[0]) ** 2)) + self.center[1]
        self.y_coordinates_positive =  np.sqrt(np.abs(self.radius ** 2 - (self.x_coordinates - self.center[0]) ** 2)) + self.center[1]

    def draw_circle(self):

        circle.calculate_circle_all_coordinates(self)

        plt.plot(self.x_coordinates, self.y_coordinates_negative,'r')
        plt.plot(self.x_coordinates, self.y_coordinates_positive,'r')
        plt.axis('scaled')