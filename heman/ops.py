import adam
from . import Image


class Ops(object):
    @staticmethod
    def stitch_horizontal(image_list):
        n = len(image_list)
        image_array = adam.HemanImageArray(n)
        for i in xrange(len(image_list)):
            image_array[i] = image_list[i].img
        # im = adam.heman_ops_stitch_horizontal(image_array, n)
        # return Image(im)

    @staticmethod
    def stitch_vertical(images):
        return None

    @staticmethod
    def normalize_f32(source, minval, maxval):
        return None

    @staticmethod
    def step(img, threshold):
        return None

    @staticmethod
    def sweep(img):
        return None
