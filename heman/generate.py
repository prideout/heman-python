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
