def draw_all_magnets(circular_magnets,rectangular_magnets):

    for magnet in circular_magnets:
        magnet.draw_circle()

    for magnet in rectangular_magnets:
        magnet.draw_rectangle('r')


