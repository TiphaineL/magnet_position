import numpy             as np
import matplotlib.pyplot as plt
from circle                import circle
from extract_mag_positions import extract_positions
from plot_plate            import plot_plate
from plot_magnets          import plot_magnets
from draw_robot_arm        import draw_robot_arm
from pickupArea_circ       import pickupArea_circ
from draw_pickupArea_circ  import drawPickupArea_circ
from pickupArea_rec        import pickupArea_rec
from draw_pickupArea_rect  import drawPickupArea_rect
from rect_corner           import rectangle_corner
from check_conflict        import conflict

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
r_circ        = 6.0                             # radius of the circular magnets
w_rect        = 12.0                            # width of the rectangular magnets
l_rect        = 20.0                            # length of the rectangular magnets
g             = 23.0                            # distance between the circular and the rectangular magnets
L             = (r_circ + g + l_rect / 2.0)     # length between center of the circ. magnet and center of rect. magnet
HECTOR_plate  = circle(0.0,0.0,260.0)
l_robot       = 14.02                           # length of the robot pick-up arm
w_robot       = 5                               # width of the robot pick-up arm
l_pickup_circ = l_robot                         # the length of the pickup area for the circular magnet
w_pickup_circ = (3.0 * w_robot / 2.0) + r_circ  # the width of the pickup rea for the circular magnet
l_pickup_rect = l_robot                         # the length of the pick up area for the rectangle magnet
w_pickup_rect = 0.5 * (l_rect + 3.0 * w_robot)  # the width of the pickup area for the rectangle magnet

####################

# Open and read file
fileName = "WithStdStars_Field 7.txt"
fileName = "WithStdStars_Field 12.txt"
fileName = 'WithStdStars_Field_test.txt'
file = open(fileName, "r")
probe, x, y, radius, angs, azAngs, angs_azAng = np.loadtxt(file, skiprows=2, unpack=True)

####################

# Extract position of the circular magnet (mag_c) and the rectangular magnet (mag_r)
mag = extract_positions(probe,x,y,angs_azAng,L)
mag = np.concatenate(mag)

# Plot the plate with the magnets
plot_plate(HECTOR_plate)
plot_magnets(r_circ,w_rect,l_rect,mag,'r')

# Plot the robot arm on top of the magnets
draw_robot_arm(mag,w_robot,l_robot)

# Calculate the pick-up areas for the circular magnets
for i in range(len(mag)):
    if mag[i][3] == 0:
        pickupArea = pickupArea_circ(w_robot, r_circ, mag[i])
        # Plot the pick-up areas for the circular magnets
        drawPickupArea_circ(pickupArea,l_robot,w_robot,r_circ)

# Calculate the pick-up areas for the rectangular magnets
for i in range(len(mag)):
    if mag[i][3] == 1:
        pickupArea = pickupArea_rec(w_robot,l_robot,l_rect,mag[i])
        # Plot the pick-up areas for the rectangular magnets
        drawPickupArea_rect(pickupArea, l_robot, w_robot, l_rect)


# Calculate the coordinates of the corners
xs   = pickupArea[0][0]
ys   = pickupArea[0][1]
angs = pickupArea[0][2]

corner_rect = rectangle_corner(xs,ys,l_pickup_rect,w_pickup_rect,angs)

# xs   = np.concatenate(pickupArea_rect[:,:,0].reshape(len(pickupArea_rect),1,2))
# ys   = np.concatenate(pickupArea_rect[:,:,1].reshape(len(pickupArea_rect),1,2))
# angs = np.concatenate(pickupArea_rect[:,:,2].reshape(len(pickupArea_rect),1,2))

# corner_rect = rectangle_corner(xs,ys,l_pickup_rect,w_pickup_rect,angs)
# corner_rect_1 = corner_rect[0]
# corner_rect_2 = corner_rect[1]
#
# #corner_rect = rectangle_corner(pickupArea_rect[0,0,0],pickupArea_rect[0,0,1],l_pickup_rect,w_pickup_rect,\
# #                               pickupArea_rect[0,0,2] )
# # print(corner_rect)




####################
# Isolate the magnets that have a close proximity to each others

# Define a minimum proximity
d0 = l_rect + w_robot

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

mag_close = np.array(mag_close)
print(mag_close)

#mag_close = np.concatenate(mag_close)
# Plot the close proximity magnets with a different colour
#plot_magnets(r_circ,w_rect,l_rect,mag_close,'m')

for pair in mag_close:
    pb = conflict(pair)












