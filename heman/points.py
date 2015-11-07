import adam
import numpy


class Points(object):
    def __init__(self, pts):
        width, height, nbands = adam.heman_image_info(pts)
        nparray = adam.heman_image_array(pts)
        self.pts = pts
        self.width = width
        self.nbands = nbands
        if nbands > 1:
            self.array = numpy.reshape(nparray, (width, height, nbands))
        else:
            self.array = numpy.reshape(nparray, (width, height))

    @classmethod
    def create(cls, arr, nbands):
        pts = adam.heman_points_create(arr, nbands)
        return Points(pts)

    def __del__(self):
        adam.heman_points_destroy(self.pts)
