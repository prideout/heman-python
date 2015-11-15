#! /usr/bin/env python

"Generate a random island."

import heman
import numpy as np
import time
import PIL.Image
import PIL.ImageDraw
import PIL.ImageEnhance


SCALE = 256


def generate_rocks(seed, nrocks):
    images = []
    for n in xrange(nrocks):
        elevation = heman.Generate.rock_heightmap(SCALE, SCALE, seed + n)
        heman.Lighting.set_occlusion_scale(5.0)
        lit = heman.Lighting.apply(elevation, None, 1, 0.5, 0.5, LIGHTPOS)
        images.append(lit)
    return heman.Ops.stitch_horizontal(images)


LIGHTPOS = (-.5, .5, 1)

if __name__ == '__main__':
    import multiprocessing
    print multiprocessing.cpu_count(), 'cores'
    start_time = time.time()
    ncols, nrows = 8, 8
    rows = []
    seed = 50
    for x in xrange(nrows):
        print 'Generating row {} / {}'.format(x, nrows)
        rows.append(generate_rocks(seed, ncols))
        seed = seed + ncols
    final = heman.Ops.stitch_vertical(rows)
    array = heman.Export.u8(final, 0, 0.925)
    im = PIL.Image.fromarray(array, 'RGB')
    im.resize((ncols * SCALE / 4, nrows * SCALE / 4)).save('atlas.png')

    elapsed = time.time() - start_time
    print('{:.3f} seconds.'.format(elapsed))
