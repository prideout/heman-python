import _heman
from . import Image


class Distance(object):
    @staticmethod
    def create_sdf(seed):
        return Image(_heman.heman_distance_create_sdf(seed.img))
