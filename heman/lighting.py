import _heman
from . import Image


class Lighting(object):
    @staticmethod
    def apply(elevation, albedo, occlusion, diffuse, softening, lightpos):
        assert len(lightpos) == 3
        x, y, z = lightpos
        return Image(_heman.heman_lighting_apply(
            elevation.img, albedo.img, occlusion,
            diffuse, softening, x, y, z))
