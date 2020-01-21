import numpy as np
from hector.probe import probe

def create_list_of_probes_from_file(file):

    probe_number, \
    circular_magnet_center_x, \
    circular_magnet_center_y, \
    radius, \
    angs, \
    azAngs, \
    rectangle_magnet_input_orientation = np.loadtxt(file, skiprows=2, unpack=True)

    list_of_probes = []

    i = 0
    for each_probe in probe_number:
        list_of_probes.append(probe(probe_number[i],
                                    [circular_magnet_center_x[i],circular_magnet_center_y[i]],
                                     rectangle_magnet_input_orientation[i]) )
        i += 1

    return list_of_probes

def create_list_of_circuar_and_rectangular_magnets_from_file(file):

    list_of_probes = create_list_of_probes_from_file(file)

    list_of_circular_magnet = []

    for each_probe in list_of_probes:
        list_of_circular_magnet.append(each_probe.extract_circular_magnet_parameters())

    list_of_rectangular_magnet = []

    for each_probe in list_of_probes:
        list_of_rectangular_magnet.append(each_probe.extract_rectangular_magnet_parameters())

    return list_of_circular_magnet,list_of_rectangular_magnet

def create_list_of_all_magnets_from_file(file):

    [circular_magnets, rectangular_magnets] = create_list_of_circuar_and_rectangular_magnets_from_file(file)

    return np.concatenate([circular_magnets, rectangular_magnets])

def get_file(filename):
    return open(filename, "r")