import _heman


def image_create(width, height, nbands):
    return _heman.heman_image_create(width, height, nbands)


def image_destroy(img):
    _heman.heman_image_destroy(img)


def image_array(img):
    return _heman.heman_image_array(img)


def generate_island_heightmap(width, height, seed):
    return _heman.heman_generate_island_heightmap(width, height, seed)
