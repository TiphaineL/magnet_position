import matplotlib.pyplot as plt
from hector.magnets.circular import is_circular_magnet
from hector.magnets.rectangular import is_rectangular_magnet

def draw_all_magnets(all_magnets):

    for magnet in all_magnets:

        if is_circular_magnet(magnet):
            magnet.draw_circle('r')
            plt.text(magnet.center[0], magnet.center[1], str(int(magnet.index)), fontsize=6)

        if is_rectangular_magnet(magnet):
            magnet.draw_rectangle('r')

def draw_magnet_pickup_areas(all_magnets,colour):

    for magnet in all_magnets:

        for pickup_area in magnet.create_pickup_areas():

            pickup_area.draw_rectangle(colour)




