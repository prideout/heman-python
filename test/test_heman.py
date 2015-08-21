import heman


def test_trivial():
    img = heman.image_create(128, 128, 1)
    heman.image_destroy(img)


def test_generate():
    island = heman.generate_island_heightmap(256, 256, 90)
    assert len(heman.image_array(island)) == 65536
    heman.image_destroy(island)
