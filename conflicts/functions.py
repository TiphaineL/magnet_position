from conflicts.magnet_pair import circle_and_circle_magnets, circle_rectangle_magnets, rectangle_rectangle_magnets
from conflicts.circular_magnet_with_circular_magnet import check_conflict_circle_circle_magnets
from conflicts.circular_magnet_with_rectangular_magnet import check_conflict_circle_rectangle_magnets
from conflicts.rectangular_magnet_and_rectangular_magnet import check_conflict_rectangle_rectangle_magnets
from hector.constants import rectangle_magnet_length, robot_arm_width
import numpy as np
from hector.magnets.rectangular import rectangular_magnet
from hector.magnets.circular import circular_magnet

def minimum_magnet_proximity():
    return rectangle_magnet_length + robot_arm_width

def calculate_magnet_to_magnet_distance(magnet1, magnet2):
    return np.sqrt((magnet2.center[0] - magnet1.center[0]) ** 2 + (magnet2.center[1] - magnet1.center[1]) ** 2)

def create_list_magnets_in_close_proximity(list_magnets):

    magnets_in_close_proximity = []

    for i in range(len(list_magnets)):
        magnet_i = list_magnets[i]

        for j in range(i+1, len(list_magnets)):
            magnet_j = list_magnets[j]

            if calculate_magnet_to_magnet_distance(magnet_i, magnet_j) < minimum_magnet_proximity():
                magnets_in_close_proximity.append([magnet_i, magnet_j])

    return np.array(magnets_in_close_proximity)

def highlight_closed_magnets_on_plot(closed_magnets, colour):

    for magnet_pair in closed_magnets:

        for magnet in magnet_pair:

            if isinstance(magnet, rectangular_magnet):
                magnet.draw_rectangle(colour)

            elif isinstance(magnet, circular_magnet):
                magnet.draw_circle(colour)

def find_conflicts_between_magnets(pair):

    all_blocked_pickup_areas = []

    if circle_and_circle_magnets(pair):

        magnet_conflict = check_conflict_circle_circle_magnets(pair)

        if magnet_conflict:

            all_blocked_pickup_areas.extend(magnet_conflict)

    elif circle_rectangle_magnets(pair):

        magnet_conflict = check_conflict_circle_rectangle_magnets(pair)

        if magnet_conflict:
            all_blocked_pickup_areas.extend(magnet_conflict)

    elif rectangle_rectangle_magnets(pair):

        magnet_conflict = check_conflict_rectangle_rectangle_magnets(pair)

        if magnet_conflict:

            all_blocked_pickup_areas.extend(magnet_conflict)

    return all_blocked_pickup_areas

def find_all_blocked_magnets(list_of_magnets):

    blocked_areas = []

    for pair in list_of_magnets:

        magnet_conflict = find_conflicts_between_magnets(pair)

        if len(magnet_conflict) > 0:
            blocked_areas.extend(magnet_conflict)