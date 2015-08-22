import _heman
from . import Image


class Color(object):
    @staticmethod
    def create_gradient(width, controlpts):
        locs = []  # TODO
        vals = []  # TODO
        img = _heman.heman_color_create_gradient(width, locs, vals)
        return Image(img)

    @staticmethod
    def apply_gradient(hmap, minv, maxv, grad):
        img = _heman.heman_color_apply_gradient(hmap.img, minv, maxc, grad.img)
        return Image(img)
