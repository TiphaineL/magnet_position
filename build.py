from magnets_functions import plot_plate
from constants import HECTOR_plate
from Operations.Extract_data import create_list_of_magnets_from_file
from Magnets.draw_all_magnets import draw_all_magnets
from Shapes.rectangle import rectangle

fileName = 'resources/WithStdStars_Field_test.txt'
file = open(fileName, "r")

[circular_magnets, rectangular_magnets] = create_list_of_magnets_from_file(file)

plot_plate(HECTOR_plate)
draw_all_magnets(circular_magnets,rectangular_magnets)

test = rectangular_magnets[0]

for magnet in circular_magnets:
   test_areas = magnet.calculate_pickup_areas()
   test_areas[0].draw_rectangle('c')
   test_areas[1].draw_rectangle('c')
   test_areas[2].draw_rectangle('c')
   test_areas[3].draw_rectangle('c')

test_areas = test.calculate_pickup_areas()
for magnet in rectangular_magnets:
    test_areas = magnet.calculate_pickup_areas()
    test_areas[0].draw_rectangle('g')
    test_areas[1].draw_rectangle('g')
