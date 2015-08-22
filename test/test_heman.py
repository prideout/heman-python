import heman
import PIL.Image
import PIL.ImageMath
import numpy as np


def test_trivial():
    img = heman.image_create(128, 128, 1)
    width, height, nbands = heman._heman.heman_image_info(img)
    assert width == 128
    assert height == 128
    assert nbands == 1
    heman.image_destroy(img)


def test_generate():
    island = heman.generate_island_heightmap(256, 256, 90)
    floats = heman.image_array(island)
    assert len(floats) == 65536
    floats = np.reshape(floats, (256, 256))
    floats = (floats + 1.0) * 0.5 * 255.0
    im = PIL.Image.fromarray(floats, 'F').convert('L')
    im.save('island.png')
    heman.image_destroy(island)


def tdd_generate():
    island = heman.Generate.island_heightmap(256, 256, 90)
    im = PIL.Image.fromarray(island.array(), 'F')
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
