from conflicts.functions import create_list_of_blocking_magnets,\
                                all_blocking_magnets_are_fully_blocked

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









