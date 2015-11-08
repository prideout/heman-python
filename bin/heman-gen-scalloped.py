#! /usr/bin/env python

"Generate a scalloped terrain."

import heman
import numpy as np
import PIL.Image
import PIL.ImageDraw
import PIL.ImageEnhance

POLITICAL_COLORS = [
    0xFFFFE0,
    0xFFEFE0,
    0xE0FFE0
]

SEED_POINTS = [
    0.5, 0.4, 0.6,
    0.2, 0.6, 0.5,
    0.8, 0.5, 0.3
]

OCEAN_COLOR = 0xB0E6FF

LIGHTPOS = (-.5, .5, 1)

DO_RESIZE = False

def generate_terrain():
    points = heman.Points.create(np.array(SEED_POINTS, dtype=np.float32), 3)
    seed = 6
    size = 768
    heman.Lighting.set_occlusion_scale(50)
    elevation, political = heman.Generate.archipelago_political(
        size, size, points, POLITICAL_COLORS, OCEAN_COLOR, seed)
    elevation = heman.Ops.emboss(elevation, -1);
    elevation = heman.Ops.stairstep(elevation, 2, 6, 1);
    political = heman.Ops.merge_political(elevation, political, OCEAN_COLOR)

    # Disable diffuse because discontinuities cause weird lighting along rims.
    final = heman.Lighting.apply(elevation, political, 1, 0, 0, LIGHTPOS)

    array = heman.Export.u8(final, 0, 1)
    im = PIL.Image.fromarray(array, 'RGB')
    if DO_RESIZE:
        im = im.resize((size / 2, size / 2))
    im.save('scalloped-rendered.png')
    array = heman.Export.u8(political, 0, 1)
    PIL.Image.fromarray(array, 'RGBA').save('scalloped-political.png')

if __name__ == '__main__':
    import multiprocessing
    print multiprocessing.cpu_count(), 'cores'
    generate_terrain()
