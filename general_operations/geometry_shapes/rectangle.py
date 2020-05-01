import matplotlib.pyplot as plt
from general_operations.trigonometry import rotational_matrix,convert_degrees_to_radians

class rectangle:

    def __init__(self,center,length,width,orientation):
        self.center = center
        self.length = length
        self.width = width
        self.orientation = orientation

    def calculate_4corners(self):

        rotation_matrix = rotational_matrix(convert_degrees_to_radians(self.orientation))

        self.corner1 = (self.center[0] - rotation_matrix[0][0] * self.width / 2 - rotation_matrix[1][0] * self.length / 2, \
                        self.center[1] - rotation_matrix[0][1] * self.width / 2 - rotation_matrix[1][1] * self.length / 2)

        self.corner2 = (self.center[0] + rotation_matrix[0][0] * self.width / 2 - rotation_matrix[1][0] * self.length / 2, \
                        self.center[1] + rotation_matrix[0][1] * self.width / 2 - rotation_matrix[1][1] * self.length / 2)

        self.corner3 = (self.center[0] + rotation_matrix[0][0] * self.width / 2 + rotation_matrix[1][0] * self.length / 2, \
                        self.center[1] + rotation_matrix[0][1] * self.width / 2 + rotation_matrix[1][1] * self.length / 2)

        self.corner4 = (self.center[0] - rotation_matrix[0][0] * self.width / 2 + rotation_matrix[1][0] * self.length / 2, \
                        self.center[1] - rotation_matrix[0][1] * self.width / 2 + rotation_matrix[1][1] * self.length / 2)

        return [self.corner1,self.corner2,self.corner3,self.corner4]


    def draw_rectangle(self,colour):

        rectangle.calculate_4corners(self)

        plt.plot([self.corner1[0], self.corner2[0]], [self.corner1[1], self.corner2[1]], colour)
        plt.plot([self.corner2[0], self.corner3[0]], [self.corner2[1], self.corner3[1]], colour)
        plt.plot([self.corner3[0], self.corner4[0]], [self.corner3[1], self.corner4[1]], colour)
        plt.plot([self.corner4[0], self.corner1[0]], [self.corner4[1], self.corner1[1]], colour)
        plt.axis('scaled')

    def plot_corners(self):

        rectangle.calculate_4corners(self)

        plt.plot(self.corner1[0], self.corner1[1],'xb')
        plt.plot(self.corner2[0], self.corner2[1], 'xb')
        plt.plot(self.corner3[0], self.corner3[1], 'xb')
        plt.plot(self.corner4[0], self.corner4[1], 'xb')

    def label_corners_on_plot(self):

        rectangle.calculate_4corners(self)

        plt.text(self.corner1[0], self.corner1[1], str(1), fontsize=15)
        plt.text(self.corner2[0], self.corner2[1], str(2), fontsize=15)
        plt.text(self.corner3[0], self.corner3[1], str(3), fontsize=15)
        plt.text(self.corner4[0], self.corner4[1], str(4), fontsize=15)