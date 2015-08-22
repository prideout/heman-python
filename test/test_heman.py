import heman
import numpy as np
import PIL.Image
import PIL.ImageDraw

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


def test_trivial():
    img = heman.Image.create(128, 128, 1)
    assert img.width == 128
    assert img.height == 128
    assert img.nbands == 1


def test_generate():
    island = heman.Generate.island_heightmap(256, 256, 90)
    floats = (island.array + 1.0) * 0.5 * 255.0
    im = PIL.Image.fromarray(floats, 'F').convert('L')
    im.save('elevation.png')


def tdd_render():
    elevation = heman.Generate.island_heightmap(256, 256, 90)
    grad = heman.Color.create_gradient(256, GRADIENT)
    albedo = heman.Color.apply_gradient(elevation, -0.5, 0.5, grad)
    final = heman.Lighting.apply(elevation, albedo, 1, 1, 0.5, LIGHTPOS)
    array = heman.Export.u8(final, 0, 1)
    im = PIL.Image.fromarray(array, 'RGB')
    im.save('island.png')


def test_distance():
    image = PIL.Image.new('L', (2048, 2028))
    draw = PIL.ImageDraw.Draw(image)
    x = 1024
    y = 1024
    r = 512
    draw.ellipse((x-r, y-r, x+r, y+r), fill=255)
    y = 512
    r = 256
    draw.ellipse((x-r, y-r, x+r, y+r), fill=255)
    y = 1024 + 512
    draw.ellipse((x-r, y-r, x+r, y+r), fill=255)
    image.save('seed.png')
    array = np.asarray(image, dtype=np.uint8)
    # seed = heman.Import.u8(array, 0, 1)
    # df = heman.Distance.create_sdf(seed)
    # PIL.Image.fromarray(heman.Export.u8(df, 0, 1), 'L').save('distance.png')
