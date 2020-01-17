import numpy             as np

import matplotlib.pyplot as plt

from magnets_functions  import extract_magnets_positions,\
                               plot_plate, plot_magnets, \
                               draw_robot_arm, \
                               calculate_circular_magnet_pickup_area, \
                               calculate_rectangle_magnet_pickup_area, \
                               draw_circular_magnet_pickup_area, \
                               draw_rectangular_magnet_pickup_area

from magnet_conflict    import conflict

from constants          import circular_magnet_radius,\
                               rectangle_magnet_length,\
                               rectangle_magnet_width,\
                               circular_rectangle_magnet_center_distance,\
                               HECTOR_plate,\
                               robot_arm_length,\
                               robot_arm_width

plt.rc('font', size=10)          # controls default text sizes
plt.rc('axes', titlesize=15)     # fontsize of the axes title
plt.rc('axes', labelsize=15)     # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)    # fontsize of the tick labels
plt.rc('ytick', labelsize=10)    # fontsize of the tick labels
plt.rc('legend', fontsize=14)    # legend fontsize
plt.rc('figure', titlesize=14)   # fontsize of the figure title

####################

# Open and read file
fileName = "resources/WithStdStars_Field 7.txt"
#fileName = "resources/WithStdStars_Field 12.txt"
fileName = 'resources/WithStdStars_Field_test.txt'
file = open(fileName, "r")

probe_number, circular_magnet_center_x, circular_magnet_center_y, radius, angs, azAngs, rectangle_orientation \
    = np.loadtxt(file, skiprows=2, unpack=True)

#probes = np.loadtxt(file, skiprows=2, unpack=True)

magnet_positions = extract_magnets_positions(probe_number, circular_magnet_center_x, circular_magnet_center_y, \
                                             rectangle_orientation, circular_rectangle_magnet_center_distance)

magnet_positions = np.concatenate(magnet_positions)
print(magnet_positions)

plot_plate(HECTOR_plate)
plot_magnets(circular_magnet_radius, rectangle_magnet_width, rectangle_magnet_length, magnet_positions, 'r')
draw_robot_arm(magnet_positions, robot_arm_width, robot_arm_length)

# Calculate the pick-up areas for the circular magnets
for i in range(len(magnet_positions)):
    if magnet_positions[i][3] == 0:
        pickupArea = calculate_circular_magnet_pickup_area(robot_arm_width, circular_magnet_radius, magnet_positions[i])
        # Plot the pick-up areas for the circular magnets
        draw_circular_magnet_pickup_area(pickupArea, robot_arm_length, robot_arm_width, circular_magnet_radius)

# Calculate the pick-up areas for the rectangular magnets
for i in range(len(magnet_positions)):
    if magnet_positions[i][3] == 1:
        pickupArea = calculate_rectangle_magnet_pickup_area(robot_arm_width, rectangle_magnet_length, magnet_positions[i])
        # Plot the pick-up areas for the rectangular magnets
        draw_rectangular_magnet_pickup_area(pickupArea, robot_arm_length, robot_arm_width, rectangle_magnet_length)

####################
# Isolate the magnets that have a close proximity to each others

# Define a minimum proximity
d0 = rectangle_magnet_length + robot_arm_width

magnets_in_close_proximity = []
i = 0
for i in range(len(magnet_positions)):
    x1 = magnet_positions[i][0]
    y1 = magnet_positions[i][1]

    for j in range(i+1, len(magnet_positions)):
        x2 = magnet_positions[j][0]
        y2 = magnet_positions[j][1]

        circular_rectangle_magnet_center_distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if circular_rectangle_magnet_center_distance < d0:
            magnets_in_close_proximity.append([magnet_positions[i], magnet_positions[j]])

magnets_in_close_proximity = np.array(magnets_in_close_proximity)

#plot_magnets(circular_magnet_radius,rectangle_magnet_width,rectangle_magnet_length,np.concatenate(magnets_in_close_proximity),'m')

for pair in magnets_in_close_proximity:
    pb = conflict(pair)












