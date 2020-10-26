import random

import pylab as plt

from lesson2.k_means import k_means
from lesson6.domain import Point
from lesson6.knn import knn

color_map = {
    0: 'r',
    1: 'b',
    2: 'g',
    3: 'y',
    4: 'm',
    5: 'c'
}


# Генерация исходных данных с помощью k-means алгоритма (lesson2)
def generate_data(points_number, clusters_number):
    points = [Point(random.randint(1, 100), random.randint(1, 100)) for i in range(points_number)]
    clustering_data = k_means(points, clusters_number, True)
    return clustering_data


# Формат обучающей и тестовой выборки отличается (поэтому рисуем по отдельности)
def show_data(general_data, test_data):
    for cluster in general_data:
        for cluster_element in cluster.elements:
            plt.scatter(cluster_element.x, cluster_element.y, color=color_map[cluster.number])
    for point in test_data:
        plt.scatter(point.x, point.y, color=color_map[point.cluster])
    plt.show()


POINTS_NUMBER = 60
CLUSTERS_NUMBER = 3
TEST_DATA_COEFFICIENT = 0.3

general_data = generate_data(POINTS_NUMBER, CLUSTERS_NUMBER)
test_data = [Point(random.randint(1, 100), random.randint(1, 100)) for i in
             range(int(POINTS_NUMBER * TEST_DATA_COEFFICIENT))]
knn(general_data, test_data, 5, 3)
show_data(general_data, test_data)
