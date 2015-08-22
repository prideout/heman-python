import _heman
import numpy


class Image(object):
    def __init__(self, img):
        width, height, nbands = _heman.heman_image_info(img)
        nparray = _heman.heman_image_array(img)
        self.img = img
        self.width = width
        self.height = height
        self.nbands = nbands
        if nbands > 1:
            self.array = numpy.reshape(nparray, (width, height, nbands))
        else:
            self.array = numpy.reshape(nparray, (width, height))

    @classmethod
    def create(cls, width, height, nbands):
        img = _heman.heman_image_create(width, height, nbands)
        return cls(img)

    def __del__(self):
        _heman.heman_image_destroy(self.img)
