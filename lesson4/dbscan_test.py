import random

from lesson4.dbscan import dbscan, noise_distribution
from lesson4.domain import Point

import matplotlib.pyplot as plt

n = 30
points = [Point(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]

color_map = {
    0: 'r',
    1: 'b',
    2: 'g',
    3: 'y',
    4: 'm',
    5: 'c',
    6: 'peru',
    7: 'gray',
    8: 'indigo',
    9: 'lime',
    10: 'pink'
}


def show(result, save):
    noise_exists = False
    for point in result:
        if point.noise:
            color = 'k'
            noise_exists = True
        else:
            color = color_map[point.cluster]
        plt.scatter(point.x, point.y, color=color)
    if noise_exists and save:
        plt.savefig("with_noise.png")
    elif save:
        plt.savefig("without_noise.png")
    plt.show()


m = 2  # default
epsilon = 25  # can change
dbscan(points, epsilon, m)
print('cluster count: ', len(set(map(lambda e: e.cluster, filter(lambda e: e.cluster is not None, points)))))
show(points, False)

noise_distribution(points)
show(points, False)
