from magnets_functions import plot_plate
from constants import HECTOR_plate
from Operations.Extract_data import create_list_of_magnets_from_file
from Magnets.draw_all_magnets import draw_all_magnets

fileName = 'resources/WithStdStars_Field_test.txt'
file = open(fileName, "r")

[circular_magnets, rectangular_magnets] = create_list_of_magnets_from_file(file)

plot_plate(HECTOR_plate)
draw_all_magnets(circular_magnets,rectangular_magnets)


