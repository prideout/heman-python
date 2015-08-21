import _heman


def image_create(width, height, nbands):
    return _heman.heman_image_create(width, height, nbands)


def image_destroy(img):
    _heman.heman_image_destroy(img)
