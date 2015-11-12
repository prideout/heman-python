#! /usr/bin/env python

import heman
import os
import json
import numpy as np
import PIL.Image
import PIL.ImageDraw

SEED = 4
COLORS = [
    0x74a99c, 0xbac270, 0x8cbb9b, 0xe59f5f,
    0x4a7957, 0xecc15e, 0xc55d55, 0x8ba578,
    0x778b52, 0x62918c, 0xb36b82, 0x7b576a,
    0x98688e, 0xf2c664, 0xffe48c, 0xc7cc8e,
    0x768e6c, 0xb29264, 0xb68c49, 0xd5847a,
    0x935225, 0xc1be81, 0x8d7a81
]


def generate_graph():
    """
    brew tap homebrew/science
    brew install graph-tool
    """

    from graph_tool.all import price_network, sfdp_layout, graph_draw
    from graph_tool.all import dfs_search, DFSVisitor, seed_rng
    from numpy.random import seed

    class AnnotationVisitor(DFSVisitor):
        def __init__(self, pred, dist):
            self.pred = pred
            self.dist = dist
            self.roots = {}

        def tree_edge(self, e):
            depth = self.dist[e.source()]
            if depth == 1:
                genre = int(e.source())
                if genre not in self.roots:
                    self.roots[genre] = len(self.roots)
            else:
                genre = self.pred[e.source()]
            self.pred[e.target()] = genre
            self.dist[e.target()] = depth + 1

    # For run-to-run stability, provide a constant seed:
    seed(SEED)
    seed_rng(SEED)

    print 'Generating graph...'
    g = price_network(2000)

    print 'Performing layout...'
    pos = sfdp_layout(g)

    print 'Adding depths...'
    dist = g.new_vertex_property("int")
    pred = g.new_vertex_property("int64_t")
    g.set_directed(False)
    visitor = AnnotationVisitor(pred, dist)
    dfs_search(g, g.vertex(0), visitor)

    print 'Iterating over verts...'
    flattened = []
    maxp = [-9999, -9999]
    minp = [+9999, +9999]
    maxd = 0
    for v in g.vertices():
        root_id = pred.a[v]
        if root_id not in visitor.roots:
            continue
        x, y, z = pos[v].a[0], pos[v].a[1], visitor.roots[root_id]
        minp[0] = min(minp[0], x)
        minp[1] = min(minp[1], y)
        maxp[0] = max(maxp[0], x)
        maxp[1] = max(maxp[1], y)
        maxd = max(maxd, dist.a[v])
        flattened += [x, y, z]

    print 'max depth is', maxd
    print 'nroots is', len(visitor.roots)
    print 'ncolors is', len(COLORS)

    extent = (maxp[0] - minp[0], maxp[1] - minp[1])
    padding = extent[0] * 0.1
    minp[0] -= padding
    minp[1] -= padding
    maxp[0] += padding
    maxp[1] += padding
    scale = [
        1.0 / (maxp[0] - minp[0]),
        1.0 / (maxp[1] - minp[1])]
    scale = min(scale[0], scale[1])
    midp = [
        0.5 * (maxp[0] + minp[0]),
        0.5 * (maxp[1] + minp[1])]
    flatarray = []
    for v in g.vertices():
        root_id = pred.a[v]
        if root_id not in visitor.roots:
            continue
        x, y, root = pos[v].a[0], pos[v].a[1], visitor.roots[root_id]
        x = (0.5 + (x - midp[0]) * scale)
        y = (0.5 + (y - midp[1]) * scale)
        prom = int(dist.a[v])
        flatarray += [x, y, root, prom]
    return flatarray


def draw_graph(flatarray, filename):
    width, height = 512, 512
    image = PIL.Image.new('RGB', (width, height))
    draw = PIL.ImageDraw.Draw(image)
    for i in xrange(0, len(flatarray), 4):
        x = width * flatarray[i]
        y = height * flatarray[i + 1]
        root = flatarray[i + 2]
        prom = flatarray[i + 3]
        c = COLORS[root % len(COLORS)]
        c = ((c & 0xff) << 16) | (c & 0xff00) | (c >> 16)
        draw.point((x, y), c)
    image.save(filename)
    print 'Produced', filename

if not os.path.exists('graph.json'):
    flatarray = generate_graph()
    json.dump(flatarray, open('graph.json', 'wt'))
    print 'Produced graph.json'

flatarray = json.load(open('graph.json', 'rt'))
draw_graph(flatarray, 'graph.png')

image = PIL.Image.open('graph.png')
array = np.asarray(image, dtype=np.uint8)
seed = heman.Import.u8(array, 0, 1)

# contour = heman_image_create(width, height, 3);
# heman_image_clear(contour, 0);
# heman.draw.contour_from_points(contour, points, colors)
# heman_draw_colored_points(contour, points, colors)

cpcf = heman.Distance.create_cpcf(seed)
voronoi = heman.Color.from_cpcf(cpcf, seed)
PIL.Image.fromarray(heman.Export.u8(voronoi, 0, 1)).save('voronoi.png')
print 'Produced voronoi.png'
