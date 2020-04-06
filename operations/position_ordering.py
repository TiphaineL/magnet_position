from conflicts.functions import create_list_of_blocking_magnets,\
                                all_blocking_magnets_are_fully_blocked
import numpy as np

def calculate_placement_ordering_of_blocked_magnet(blocked_magnet,list_of_conflicts,list_of_fully_blocked_magnets):

    blocking_magnets = create_list_of_blocking_magnets(list_of_conflicts, blocked_magnet)

    for i in range(50):

        if not all_blocking_magnets_are_fully_blocked(blocking_magnets,list_of_fully_blocked_magnets):

            blocked_magnet.placement_index += 1

            break

        else:

            blocking_magnets = []

            for magnet in blocking_magnets:
                blocking_magnets.append(create_list_of_blocking_magnets(list_of_conflicts, magnet))

    if i == 49:
        blocked_magnet.placement_index = None
        print('Error ! ',blocked_magnet.__class__.__name__,int(blocked_magnet.index),' cannot be placed')

def calculate_placement_ordering_of_all_blocked_magnets(list_of_fully_blocked_magnets,list_of_conflicts):

    for blocked_magnet in list_of_fully_blocked_magnets:
        calculate_placement_ordering_of_blocked_magnet(blocked_magnet,list_of_conflicts,list_of_fully_blocked_magnets)

def create_positioning_array(all_magnets, fully_blocked_magnets, conflicted_magnets):

    calculate_placement_ordering_of_all_blocked_magnets(fully_blocked_magnets, conflicted_magnets)

    max_order = max(magnet.placement_index for magnet in all_magnets if magnet.placement_index is not None)

    ordering_array = []
    for magnet in all_magnets:

        available_pickup = [area.code for area in magnet.pickup_areas]

        if magnet.placement_index == None:
            ordering_array.append(np.append([magnet.__class__.__name__, int(magnet.index), None],available_pickup))

        else:
            order = 1
            for increment in range(max_order + 1):
                if magnet.placement_index == max_order - increment:
                    order += increment
                    f = np.append([magnet.__class__.__name__, int(magnet.index), str(order)],available_pickup)
                    ordering_array.append(np.array(f))

    return np.array(ordering_array)





