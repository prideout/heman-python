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
    def step(img, threshold):
        return Image(adam.heman_ops_step(img.img, threshold))

    @staticmethod
    def sweep(img):
        return Image(adam.heman_ops_sweep(img.img))

    @staticmethod
    def stairstep(img, nsteps_water, nsteps_land):
        return Image(adam.heman_ops_stairstep(img.img, nsteps_water,
                     nsteps_land))
