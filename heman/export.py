import adam
import numpy
from . import Image


class Export(object):
    @staticmethod
    def u8(img, minv, maxv):
        width, height, nbands = adam.heman_image_info(img.img)
        arr = numpy.zeros(width * height * nbands, dtype=numpy.uint8)
        adam.heman_export_u8(img.img, minv, maxv, arr)
        if nbands > 1:
            return numpy.reshape(arr, (width, height, nbands))
        return numpy.reshape(arr, (width, height))


class Import(object):
    @staticmethod
    def u8(arr, minv, maxv):
        nbands = 1
        if len(arr.shape) > 2:
            nbands = arr.shape[2]
        width, height = arr.shape[:2]
        arr = numpy.reshape(arr, width * height * nbands)
        img = adam.heman_import_u8(width, height, nbands, arr, minv, maxv)
        return Image(img)
