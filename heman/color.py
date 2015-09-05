import adam
from . import Image


class Color(object):
    @staticmethod
    def create_gradient(width, controlpts):
        assert len(controlpts) >= 2
        assert 0 == (len(controlpts) % 2)
        locs = controlpts[::2]
        vals = controlpts[1::2]
        img = adam.heman_color_create_gradient(width, locs, vals)
        return Image(img)

    @staticmethod
    def apply_gradient(hmap, minv, maxv, grad):
        img = adam.heman_color_apply_gradient(hmap.img, minv, maxv, grad.img)
        return Image(img)

    @staticmethod
    def set_gamma(f):
        adam.heman_color_set_gamma(f)
