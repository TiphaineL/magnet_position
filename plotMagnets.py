import numpy as np
import matplotlib.pyplot as plt
from circle import circle
from extract_mag_positions import extract_positions
from plot_plateWmagnets import plot_plate_with_magnets
from draw_robot_arm import draw_robot_arm
from pickupArea_circ import pickupArea_circ
from draw_pickupArea_circ import drawPickupArea_circ
from pickupArea_rec import pickupArea_rec

# This code reads the position of the magnets from the text file and plot them

plt.rc('font', size=10)          # controls default text sizes
plt.rc('axes', titlesize=15)     # fontsize of the axes title
plt.rc('axes', labelsize=15)     # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)    # fontsize of the tick labels
plt.rc('ytick', labelsize=10)    # fontsize of the tick labels
plt.rc('legend', fontsize=14)    # legend fontsize
plt.rc('figure', titlesize=14)   # fontsize of the figure title

#####################

# Dimensions of interest
r_circ = 6.0                          # radius of the circular magnets
w_rect = 12.0                         # width of the rectangular magnets
l_rect = 20.0                         # length of the rectangular magnets
g = 23.0                              # distance between the circular and the rectangular magnets
L = (r_circ + g + l_rect / 2.0)       # length between center of the circ. magnet and center of rect. magnet
HECTOR_plate = circle(0.0,0.0,260.0)
l_robot = 14.02                       # length of the robot pick-up arm
w_robot = 5                           # width of the robot pick-up arm

####################

# Open and read file
fileName = "WithStdStars_Field 7.txt"
fileName = "WithStdStars_Field 12.txt"
file = open(fileName, "r")
probe, x, y, radius, angs, azAngs, angs_azAng = np.loadtxt(file, skiprows=2, unpack=True)

####################

# Extract position of the circular magnet (mag_c) and the rectangular magnet (mag_r)
mag = extract_positions(probe,x,y,angs_azAng,L)
mag_c = mag[0]
mag_r = mag[1]

# Plot the plate with the magnets
plot_plate_with_magnets(r_circ,w_rect,l_rect,HECTOR_plate,mag_c,mag_r)

# Plot the robot arm on top of the magnets
# draw_robot_arm(mag_c,mag_r,w_robot,l_robot)

# Calculate the pick-up areas for the circular magnets
pickupArea_circ = pickupArea_circ(w_robot,r_circ,mag_c)

# Plot the pick-up areas for the circular magnets
drawPickupArea_circ(pickupArea_circ,l_robot,w_robot,r_circ)

# Plot the pick-up areas for the rectangular magnets
pickupArea_rec(w_robot,l_robot,l_rect,mag_r)

####################
# Isolate the magnets that have a close proximity to each others

# Define a minimum proximity
d0 = l_rect + w_robot

mag = np.concatenate(mag)

mag_close = []
i = 0
for i in range(len(mag)):
    x1 = mag[i][0]
    y1 = mag[i][1]

    for j in range(i+1,len(mag)):
        x2 = mag[j][0]
        y2 = mag[j][1]

        L = np.sqrt( (x2-x1)**2 + (y2-y1)**2 )

        if L < d0:
            mag_close.append([mag[i],mag[j]])

print(np.array(mag_close))




