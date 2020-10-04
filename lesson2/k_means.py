import matplotlib.pyplot as plt
import numpy as np

from lesson2.domain import Point, Cluster
from lesson2.functions import dist

color_map = {
    0: 'r',
    1: 'b',
    2: 'g',
    3: 'y',
    4: 'm',
    5: 'k'
}


def init_clusters(k):
    clusters_result = []
    for i in range(0, k):
        clusters_result.append(Cluster([], i, color_map.get(i)))
    return clusters_result


def check_stop_clustering(clusters):
    return all(element for element in
               list((map(
                   lambda e: e.last_x_center == e.x_center is not None and e.last_y_center == e.y_center is not None,
                   clusters))))


def update_clusters(clusters, centroids):
    k = len(clusters)
    for clust in clusters:
        clust.clean_elements()
    for i in range(0, k):
        clusters[i].last_x_center = clusters[i].x_center
        clusters[i].last_y_center = clusters[i].y_center
        clusters[i].x_center = centroids[i].x
        clusters[i].y_center = centroids[i].y


def cluster_iteration(coordinates, centroids, clusters):
    n = len(coordinates)
    k = len(clusters)
    update_clusters(clusters, centroids)
    for i in range(0, n):
        d = dist(coordinates[i].x, coordinates[i].y, centroids[0].x, centroids[0].y)
        cluster_num = 0
        for j in range(0, k):
            if dist(coordinates[i].x, coordinates[i].y, centroids[j].x, centroids[j].y) < d:
                d = dist(coordinates[i].x, coordinates[i].y, centroids[j].x, centroids[j].y)
                cluster_num = j
        list(filter(lambda e: e.number == cluster_num, clusters))[0].add_element(coordinates[i])


def find_centroid(clusters, k):
    x_cc = []
    y_cc = []
    for cluster in clusters:
        x_cc.append(np.mean(list(map(lambda e: e.x, cluster.elements))))
        y_cc.append(np.mean(list(map(lambda e: e.y, cluster.elements))))
    result = []
    for i in range(0, k):
        result.append(Point(x_cc[i], y_cc[i]))
    return result


def init_centroid(coordinates, k, x_center, y_center):
    R = 0
    n = len(coordinates)
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


def k_means(coordinates, k, show=True):
    init_clusters(k)

    x_center = np.mean(list(map(lambda e: e.x, coordinates)))
    y_center = np.mean(list(map(lambda e: e.y, coordinates)))

    first_iteration = True

    clusters = init_clusters(k)
    while not check_stop_clustering(clusters):
        if first_iteration:
            centroids = init_centroid(coordinates, k, x_center, y_center)
            first_iteration = False
        else:
            centroids = find_centroid(clusters, k)
        cluster_iteration(coordinates, centroids, clusters)

    if show:
        for current_cluster in clusters:
            for point in current_cluster.elements:
                plt.scatter(point.x, point.y, color=current_cluster.color)
        plt.show()

    return clusters
