import adam
from . import Image


class Generate(object):
    @staticmethod
    def island_heightmap(width, height, seed):
        img = adam.heman_generate_island_heightmap(width, height, seed)
        return Image(img)

    @staticmethod
    def simplex_fbm(width, height, frequency, amplitude, octaves, lacunarity,
                    gain, seed):
        img = adam.heman_generate_simplex_fbm(
            width, height, frequency,
            amplitude, octaves, lacunarity, gain, seed)
        return Image(img)

    @staticmethod
    def planet_heightmap(width, height, seed):
        img = adam.heman_generate_planet_heightmap(width, height, seed)
        return Image(img)

    @staticmethod
    def archipelago_heightmap(width, height, points, noiseamt, seed):
        img = adam.heman_generate_archipelago_heightmap(
            width, height, points.pts, noiseamt, seed)
        return Image(img)

    @staticmethod
    def archipelago_political(width, height, points, colors, ocean_color,
                              seed):

        political = adam.heman_generate_archipelago_political_1(
            width, height, points.pts, colors, ocean_color, seed)

        elevation = adam.heman_generate_archipelago_political_2(
            width, height, ocean_color, seed, political)

        return Image(elevation), Image(political)
