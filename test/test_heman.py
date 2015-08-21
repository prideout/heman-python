import heman


def test_heman():
    img = heman.image_create(128, 128, 1)
    heman.image_destroy(img)
