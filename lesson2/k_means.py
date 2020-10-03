import random

import matplotlib.pyplot as plt
import numpy as np

from lesson2.domain import Point, Cluster

n, k = 100, 4
color_map = {
    0: 'r',
    1: 'b',
    2: 'g',
    3: 'y'
}
coordinates = [Point(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]

x_center = np.mean(list(map(lambda e: e.x, coordinates)))
y_center = np.mean(list(map(lambda e: e.y, coordinates)))


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def init_clusters():
    clusters_result = []
    for i in range(0, k):
        clusters_result.append(Cluster([], i, color_map.get(i)))
    return clusters_result


def check_stop_clustering(clusters):
    return all(element for element in
               list((map(lambda e: e.last_x_center == e.x_center is not None and e.last_y_center == e.y_center is not None,
                         clusters))))


def find_centroid(clusters):
    x_cc = []
    y_cc = []
    for cluster in clusters:
        x_cc.append(np.mean(list(map(lambda e: e.x, cluster.elements))))
        y_cc.append(np.mean(list(map(lambda e: e.y, cluster.elements))))
    result = []
    for i in range(0, k):
        result.append(Point(x_cc[i], y_cc[i]))
    return result


def update_clusters(clusters, centroids):
    for clust in clusters:
        clust.clean_elements()
    for i in range(0, k):
        clusters[i].last_x_center = clusters[i].x_center
        clusters[i].last_y_center = clusters[i].y_center
        clusters[i].x_center = centroids[i].x
        clusters[i].y_center = centroids[i].y


def cluster_iteration(coordinates, centroids, clusters):
    update_clusters(clusters, centroids)
    for i in range(0, n):
        d = dist(coordinates[i].x, coordinates[i].y, centroids[0].x, centroids[0].y)
        cluster_num = 0
        for j in range(0, k):
            if dist(coordinates[i].x, coordinates[i].y, centroids[j].x, centroids[j].y) < d:
                d = dist(coordinates[i].x, coordinates[i].y, centroids[j].x, centroids[j].y)
                cluster_num = j
        list(filter(lambda e: e.number == cluster_num, clusters))[0].add_element(coordinates[i])


def init_centroid(coordinates):
    R = 0
    for i in range(0, n):
        r = dist(x_center, y_center, coordinates[i].x, coordinates[i].y)
        if r > R:
            R = r
    x_cc = [R * np.cos(2 * np.pi * i / k) + x_center for i in range(k)]
    y_cc = [R * np.sin(2 * np.pi * i / k) + y_center for i in range(k)]
    result = []
    for i in range(0, k):
        result.append(Point(x_cc[i], y_cc[i]))
    return result


first_iteration = True

clusters = init_clusters()
while not check_stop_clustering(clusters):
    if first_iteration:
        centroids = init_centroid(coordinates)
        first_iteration = False
    else:
        centroids = find_centroid(clusters)
    cluster_iteration(coordinates, centroids, clusters)

for current_cluster in clusters:
    for point in current_cluster.elements:
        plt.scatter(point.x, point.y, color=current_cluster.color)

plt.show()
