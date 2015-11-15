import adam
from . import Image


class Lighting(object):
    @staticmethod
    def apply(elevation, albedo, occlusion, diffuse, softening, lightpos):
        assert len(lightpos) == 3
        x, y, z = lightpos
        albedo = albedo.img if albedo else None
        return Image(adam.heman_lighting_apply(
            elevation.img, albedo, occlusion,
            diffuse, softening, x, y, z))

    @staticmethod
    def set_occlusion_scale(s):
        adam.heman_lighting_set_occlusion_scale(s)

    @staticmethod
    def compute_occlusion(elevation):
        assert elevation.nbands == 1
        return Image(adam.heman_lighting_compute_occlusion(elevation.img))

    @staticmethod
    def compute_normals(elevation):
        assert elevation.nbands == 1
        return Image(adam.heman_lighting_compute_normals(elevation.img))
