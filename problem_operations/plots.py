import matplotlib.pyplot as plt
from hector.magnets.circular import is_circular_magnet
from hector.magnets.rectangular import is_rectangular_magnet

plt.rc('font', size=30)          # controls default text sizes
plt.rc('axes', titlesize=30)     # fontsize of the axes title
plt.rc('axes', labelsize=30)     # fontsize of the x and y labels
plt.rc('xtick', labelsize=30)    # fontsize of the tick labels
plt.rc('ytick', labelsize=30)    # fontsize of the tick labels
plt.rc('legend', fontsize=30)    # legend fontsize
plt.rc('figure', titlesize=30)   # fontsize of the figure title

def draw_all_magnets(magnets):

    for magnet in magnets:

        if is_circular_magnet(magnet):
            magnet.draw_circle('r')
            #plt.text(magnet.center[0], magnet.center[1], str(int(magnet.index)), fontsize=15)

        if is_rectangular_magnet(magnet):
            magnet.draw_rectangle('r')
            #plt.text(magnet.center[0], magnet.center[1], str(int(magnet.index)), fontsize=15)

            plt.xlabel('mm')
            plt.ylabel('mm')

def draw_magnet_pickup_areas(magnets, colour):

    for magnet in magnets:
        magnet.create_pickup_areas()
        for pickup_area in magnet.pickup_areas:
            pickup_area.draw_rectangle(colour)




