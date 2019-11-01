import numpy as np
import math
import matplotlib.pyplot as plt
from circle import circle
from plot_plateWmagnets import plot_plate_with_magnets

# This code reads the position of the magnets from the text file and plot them

plt.rc('font', size=10)          # controls default text sizes
plt.rc('axes', titlesize=15)     # fontsize of the axes title
plt.rc('axes', labelsize=15)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)    # fontsize of the tick labels
plt.rc('ytick', labelsize=10)    # fontsize of the tick labels
plt.rc('legend', fontsize=14)    # legend fontsize
plt.rc('figure', titlesize=14)  # fontsize of the figure title

##################### Dimensions of interest
r_circ = 6.0 # radius of the circular magnets
w_rect = 12.0 # width of the rectangular magnets
l_rect = 20.0 # length of the rectangular magnets
g = 23.0 # distance between the circular and the rectangular magnets
L = (r_circ + g + l_rect / 2.0) # length between center of the circ. magnet and center of rect. magnet
HECTOR_plate = circle(0.0,0.0,260.0)
l_robot = 14.02 # length of the robot pick-up arm
w_robot = 5 # width of the robot pick-up arm
####################

# Open and read file
fileName = "WithStdStars_Field 7.txt"
fileName = "WithStdStars_Field 12.txt"
file = open(fileName, "r")
probe, x, y, radius, angs, azAngs, angs_azAng = np.loadtxt(file, skiprows=2, unpack=True)

plot_plate_with_magnets(r_circ,w_rect,l_rect,g,L,HECTOR_plate,l_robot,w_robot,
                        probe, x, y, radius, angs, azAngs, angs_azAng)


