import _heman
from . import Image


class Generate(object):
    @staticmethod
    def island_heightmap(width, height, seed):
        img = _heman.heman_generate_island_heightmap(width, height, seed)
        return Image(img)
