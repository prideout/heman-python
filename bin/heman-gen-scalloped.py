#! /usr/bin/env python

"Generate a scalloped terrain."

import heman
import numpy as np
import PIL.Image


def generate_terrain():

    elevation = heman.Generate.island_heightmap(1024, 1024, 90)

    points = [
        0.5, 0.4, 0.4,
        0.3, 0.5, 0.6,
        0.7, 0.7, 0.2,
    ]
    noiseamt = 0.5
    seed = 123

    # elevation = heman.Generate.archipelago_heightmap(
    #     800, 450, points, noiseamt, seed)

    grad = heman.Color.create_gradient(256, GRADIENT)
    albedo = heman.Color.apply_gradient(elevation, -0.5, 0.5, grad)
    final = heman.Lighting.apply(elevation, albedo, 1, 1, 0.5, LIGHTPOS)
    array = heman.Export.u8(final, 0, 1)
    im = PIL.Image.fromarray(array, 'RGB')
    im.save('scalloped.png')

GRADIENT = [
    000, 0x001070,
    126, 0x2C5A7C,
    127, 0xE0F0A0,
    128, 0x5D943C,
    160, 0x606011,
    200, 0xFFFFFF,
    255, 0xFFFFFF,
]

LIGHTPOS = (-.5, .5, 1)

if __name__ == '__main__':
    import multiprocessing
    print multiprocessing.cpu_count(), 'cores'
    generate_terrain()
