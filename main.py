import sys
sys.path.append('/Users/tiphaine/Desktop/HECTOR/magnet_position_and_conflict/')

from problem_operations.conflicts.functions import find_all_blocked_magnets,\
                                    create_list_of_fully_blocked_magnets
from problem_operations.conflicts.blocked_magnet import print_fully_blocked_magnets
from problem_operations.extract_data import create_list_of_all_magnets_from_file,get_file
from problem_operations.plots import draw_magnet_pickup_areas, draw_all_magnets
from problem_operations.position_ordering import create_position_ordering_array
from hector.plate import HECTOR_plate

plate_file = get_file('galaxy_fields/WithStdStars_Field 12.txt')

all_magnets = create_list_of_all_magnets_from_file(plate_file)

HECTOR_plate().draw_circle('r')
draw_magnet_pickup_areas(all_magnets, '--c')
draw_all_magnets(all_magnets)

conflicted_magnets = find_all_blocked_magnets(all_magnets)

fully_blocked_magnets = create_list_of_fully_blocked_magnets(conflicted_magnets)
print_fully_blocked_magnets(fully_blocked_magnets)

positioning_array = create_position_ordering_array(all_magnets, fully_blocked_magnets, conflicted_magnets)

print(positioning_array)

#import csv
#with open('magnets_positioning_order.csv','w') as conflicts:
#    writer = csv.writer(conflicts, delimiter='\t')
#    writer.writerows(positioning_array)






