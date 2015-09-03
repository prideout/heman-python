import adam
from . import Image


class Lighting(object):
    @staticmethod
    def apply(elevation, albedo, occlusion, diffuse, softening, lightpos):
        assert len(lightpos) == 3
        x, y, z = lightpos
        return Image(adam.heman_lighting_apply(
            elevation.img, albedo.img, occlusion,
            diffuse, softening, x, y, z))

    @staticmethod
    def compute_occlusion(elevation):
        assert elevation.nbands == 1
        return Image(adam.heman_lighting_compute_occlusion(elevation.img))
