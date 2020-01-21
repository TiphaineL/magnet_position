from conflicts.functions     import create_list_magnets_in_close_proximity,\
                                    highlight_closed_magnets_on_plot,\
                                    find_all_blocked_magnets
from hector.plate            import HECTOR_plate
from operations.extract_data import create_list_of_all_magnets_from_file,\
                                    get_file
from operations.draw         import draw_all_magnets,\
                                    draw_magnet_pickup_areas

file = get_file('galaxy_fields/WithStdStars_Field_test.txt')

list_of_all_magnets = create_list_of_all_magnets_from_file(file)

HECTOR_plate().draw_circle('r')

draw_magnet_pickup_areas(list_of_all_magnets,'y')
draw_all_magnets(list_of_all_magnets)

magnets_in_close_proximity = create_list_magnets_in_close_proximity(list_of_all_magnets)
highlight_closed_magnets_on_plot(magnets_in_close_proximity, 'c')

blocked_magnets = find_all_blocked_magnets(magnets_in_close_proximity)




