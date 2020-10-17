import random

from lesson4.dbscan import dbscan, noise_distribution
from lesson4.domain import Point

import matplotlib.pyplot as plt

n = 60
points = [Point(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]

color_map = {
    0: 'r',
    1: 'b',
    2: 'g',
    3: 'y',
    4: 'm',
    5: 'c',
    6: 'peru'

}


def show(result):
    noise_exists = False
    for point in result:
        if point.noise:
            color = 'k'
            noise_exists = True
        else:
            color = color_map[point.cluster]
        plt.scatter(point.x, point.y, color=color)
    if noise_exists:
        plt.savefig("with_noise.png")
    else:
        plt.savefig("without_noise.png")
    plt.show()


dbscan(points, 40, 7)
print('cluster count: ', len(set(map(lambda e: e.cluster, filter(lambda e: e.cluster is not None, points)))))
show(points)

noise_distribution(points)
show(points)
