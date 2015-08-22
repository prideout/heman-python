import heman
import PIL.Image
import PIL.ImageMath
import numpy as np


def test_trivial():
    img = heman.Image.create(128, 128, 1)
    assert img.width == 128
    assert img.height == 128
    assert img.nbands == 1


def test_generate():
    island = heman.Generate.island_heightmap(256, 256, 90)
    floats = (island.array + 1.0) * 0.5 * 255.0
    im = PIL.Image.fromarray(floats, 'F').convert('L')
    im.save('elevation.png')  # todo save an exr too


def tdd_render():
    elevation = heman.Generate.island_heightmap(256, 256, 90)
    # gradient stuff here...
    lightpos = (-.5, .5, 1)
    final = heman.Lighting.apply(elevation, albedo, 1, 1, 0.5, lightpos)
    array = heman.Export.u8(final, 0, 1)
    im = PIL.Image.fromarray(array, 'RGB')
    im.save('island.png')


def tdd_distance():
    # draw a monochrome image using PIL...
    pass
