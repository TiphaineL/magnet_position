import sys
sys.path.append('/Users/tiphaine/Desktop/HECTOR/magnet_position_and_conflict/')

from conflicts.functions     import find_all_blocked_magnets,\
                                    create_list_of_fully_blocked_magnets
from conflicts.blocked_magnet import print_fully_blocked_magnets
from operations.extract_data import create_list_of_all_magnets_from_file,get_file
from operations.draw import draw_magnet_pickup_areas, draw_all_magnets
from operations.position_ordering import create_positioning_array
from hector.plate import HECTOR_plate

plate_file = get_file('galaxy_fields/WithStdStars_Field_test.txt')

all_magnets = create_list_of_all_magnets_from_file(plate_file)

HECTOR_plate().draw_circle('r')
draw_magnet_pickup_areas(all_magnets, 'y')
draw_all_magnets(all_magnets)

conflicted_magnets = find_all_blocked_magnets(all_magnets)

fully_blocked_magnets = create_list_of_fully_blocked_magnets(conflicted_magnets)
print_fully_blocked_magnets(fully_blocked_magnets)

positioning_array = create_positioning_array(all_magnets, fully_blocked_magnets, conflicted_magnets)

import csv
with open('magnets_positioning_order.csv','w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(positioning_array)
quit()





