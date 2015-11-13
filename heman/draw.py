import adam
from . import Image


class Draw(object):

    @staticmethod
    def points(target, pts, val):
        adam.heman_draw_points(target.img, pts.pts, val)

    @staticmethod
    def splats(target, pts, radius, mode):
        adam.heman_draw_splats(target.img, pts.pts, radius, mode)

    @staticmethod
    def colored_points(target, coords, colors):
        adam.heman_draw_colored_points(target.img, coords.pts, colors)

    @staticmethod
    def contour_from_points(target, coords, color, mind, maxd, filterd):
        adam.heman_draw_contour_from_points(
            target.img, coords.pts, color, mind, maxd, filterd)
