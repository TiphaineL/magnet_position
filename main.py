import sys
sys.path.append('/Users/tiphaine/Desktop/HECTOR/magnet_position_and_conflict/')
from conflicts.functions     import create_list_magnets_in_close_proximity,\
                                    highlight_closed_magnets_on_plot,\
                                    find_all_blocked_magnets,\
                                    create_list_of_fully_blocked_magnets
from conflicts.blocked_magnet import print_fully_blocked_magnets
from conflicts.test          import calculate_placement_ordering_of_all_blocked_magnets
from operations.extract_data import create_list_of_all_magnets_from_file,\
                                    get_file

from hector.plate import HECTOR_plate
from operations.draw import draw_magnet_pickup_areas, draw_all_magnets


file = get_file('galaxy_fields/WithStdStars_Field_test.txt')

list_of_all_magnets = create_list_of_all_magnets_from_file(file)

HECTOR_plate().draw_circle('r')

for magnet in list_of_all_magnets:

    magnet.create_pickup_areas()

#draw_magnet_pickup_areas(list_of_all_magnets,'y')
#draw_all_magnets(list_of_all_magnets)

magnets_in_close_proximity = create_list_magnets_in_close_proximity(list_of_all_magnets)
#highlight_closed_magnets_on_plot(magnets_in_close_proximity,'c')

list_of_conflicted_magnets = find_all_blocked_magnets(magnets_in_close_proximity)

for conflict in list_of_conflicted_magnets:
    if conflict.blocked_pickup_area in conflict.blocked_magnet.pickup_areas:
        conflict.blocked_magnet.pickup_areas.remove(conflict.blocked_pickup_area)

draw_magnet_pickup_areas(list_of_all_magnets,'y')
draw_all_magnets(list_of_all_magnets)

fully_blocked_magnet = create_list_of_fully_blocked_magnets(list_of_conflicted_magnets)

print_fully_blocked_magnets(fully_blocked_magnet)



#calculate_placement_ordering_of_all_blocked_magnets(fully_blocked_magnet,list_of_conflicted_magnets)

#print('Magnets are placed by descending placement order number. (ie. large placement order numbers are placed first).')
#for magnet in list_of_all_magnets:
#    print(magnet.__class__.__name__,int(magnet.index),' placement order ',magnet.placement_index)




