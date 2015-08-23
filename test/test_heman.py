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

    # Create a 1 band image, which translates to a 2D numpy array.
    img = heman.Image.create(32, 48, 1)
    assert img.width == 32
    assert img.height == 48
    assert img.nbands == 1
    assert img.array.shape == (32, 48)

    # Create a multi-band image, which translates to a 3D numpy array.
    img = heman.Image.create(32, 48, 3)
    assert img.width == 32
    assert img.height == 48
    assert img.nbands == 3
    assert img.array.shape == (32, 48, 3)


def test_generate():

    # Generate a random height field whose values are in [-1, +1].
    island = heman.Generate.island_heightmap(256, 256, 90)

    # Perform a manual conversion of the F32 image to U8.
    fparray = (island.array + 1.0) * 0.5 * 255.0
    PIL.Image.fromarray(fparray).convert('L').save('elevation0.png')

    # Now, try a more convenient way of doing the same thing.
    u8array = heman.Export.u8(island, -1, 1)
    PIL.Image.fromarray(u8array).save('elevation1.png')


def test_render():
    elevation = heman.Generate.island_heightmap(256, 256, 90)
    grad = heman.Color.create_gradient(256, GRADIENT)
    albedo = heman.Color.apply_gradient(elevation, -0.5, 0.5, grad)
    final = heman.Lighting.apply(elevation, albedo, 1, 1, 0.5, LIGHTPOS)
    array = heman.Export.u8(final, 0, 1)
    im = PIL.Image.fromarray(array, 'RGB')
    im.save('island.png')


def test_distance():
    image = PIL.Image.new('L', (2048, 2048))
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
    seed = heman.Import.u8(array, 0, 1)
    df = heman.Distance.create_sdf(seed)
    PIL.Image.fromarray(heman.Export.u8(df, -1, 1)).save('distance.png')
