#! /usr/bin/env python

"Generate a scalloped terrain."

import heman
import numpy as np
import PIL.Image

POLITICAL_COLORS = [
    0x92A35F,
    0xBFD671,
    0xD8F590
]

SEED_POINTS = [
    0.5, 0.5, 0.4,
    0.7, 0.7, 0.8,
    0.8, 0.2, 0.1
]

OCEAN_COLOR = 0xB0E6FF

LIGHTPOS = (-.5, .5, 1)

def generate_terrain():
    points = heman.Points.create(np.array(SEED_POINTS, dtype=np.float32), 3)
    noiseamt = 0.5
    seed = 2
    elevation, political = heman.Generate.archipelago_political(
        1024, 1024, points, POLITICAL_COLORS, OCEAN_COLOR, noiseamt, seed)
    elevation = heman.Ops.stairstep(elevation, 2, 6, 1);
    political = heman.Ops.merge_political(elevation, political, OCEAN_COLOR)
    heman.Lighting.set_occlusion_scale(20)
    final = heman.Lighting.apply(elevation, political, 1, 1, 0.5, LIGHTPOS)
    array = heman.Export.u8(final, 0, 1)
    im = PIL.Image.fromarray(array, 'RGB')
    im.save('scalloped-rendered.png')

    array = heman.Export.u8(political, 0, 1)
    PIL.Image.fromarray(array, 'RGBA').save('scalloped-political.png')

if __name__ == '__main__':
    import multiprocessing
    print multiprocessing.cpu_count(), 'cores'
    generate_terrain()
