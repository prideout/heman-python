import adam
from . import Image


class Distance(object):
    @staticmethod
    def create_sdf(seed):
        return Image(adam.heman_distance_create_sdf(seed.img))
