import adam
from . import Image


class Generate(object):
    @staticmethod
    def island_heightmap(width, height, seed):
        img = adam.heman_generate_island_heightmap(width, height, seed)
        return Image(img)
