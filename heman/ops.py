import adam
from . import Image


class Ops(object):
    @staticmethod
    def stitch_horizontal(image_list):
        n = len(image_list)
        image_array = adam.HemanImageArray(n)
        for i in xrange(len(image_list)):
            image_array[i] = image_list[i].img
        im = adam.heman_ops_stitch_horizontal(image_array.cast(), n)
        return Image(im)

    @staticmethod
    def stitch_vertical(image_list):
        n = len(image_list)
        image_array = adam.HemanImageArray(n)
        for i in xrange(len(image_list)):
            image_array[i] = image_list[i].img
        im = adam.heman_ops_stitch_vertical(image_array.cast(), n)
        return Image(im)

    @staticmethod
    def normalize_f32(source, minval, maxval):
        return Image(adam.heman_ops_normalize_f32(source.img, minval, maxval))

    @staticmethod
    def max(imga, imgb):
        return Image(adam.heman_ops_max(imga.img, imgb.img))

    @staticmethod
    def step(img, threshold):
        return Image(adam.heman_ops_step(img.img, threshold))

    @staticmethod
    def sweep(img):
        return Image(adam.heman_ops_sweep(img.img))

    @staticmethod
    def stairstep(img, nsteps, mask, mask_color, invert_mask, offset):
        if mask:
            adam.heman_ops_stairstep(
                img.img, nsteps, mask.img, mask_color, invert_mask, offset)
        else:
            adam.heman_ops_stairstep(
                img.img, nsteps, None, mask_color, invert_mask, offset)

    @staticmethod
    def percentiles(img, nsteps, mask, mask_color, invert_mask, offset):
        if mask:
            adam.heman_ops_percentiles(
                img.img, nsteps, mask.img, mask_color, invert_mask, offset)
        else:
            adam.heman_ops_percentiles(
                img.img, nsteps, None, mask_color, invert_mask, offset)

    @staticmethod
    def merge_political(elevation, political, ocean_color):
        img = adam.heman_ops_merge_political(elevation.img, political.img,
                                             ocean_color)
        return Image(img)

    @staticmethod
    def emboss(elevation, mode):
        return Image(adam.heman_ops_emboss(elevation.img, mode))

    @staticmethod
    def sobel(src, beach_color):
        return Image(adam.heman_ops_sobel(src.img, beach_color))

    @staticmethod
    def warp(src, seed, noctaves):
        return Image(adam.heman_ops_warp(src.img, seed, noctaves))

    @staticmethod
    def warp_points(src, seed, noctaves, points):
        return Image(adam.heman_ops_warp_points(
            src.img, seed, noctaves, points.pts))
