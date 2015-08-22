import _heman
import numpy


class Export(object):
    @staticmethod
    def u8(img, minv, maxv):
        width, height, nbands = _heman.heman_image_info(img.img)
        arr = numpy.zeros(width * height * nbands, dtype=numpy.uint8)
        _heman.heman_export_u8(img.img, minv, maxv, arr)
        return numpy.reshape(arr, (width, height, nbands))
