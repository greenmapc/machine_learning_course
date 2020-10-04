import random

from lesson2.domain import Point
from lesson2.k_means import dist, k_means
import matplotlib.pyplot as plt


def objective_function(clusters):
    function_result = 0
    for cluster in clusters:
        for point in cluster.elements:
            point_dist = dist(point.x, point.y, cluster.x_center, cluster.y_center)
            function_result += point_dist * point_dist
    return function_result


def show_objective_function_plt(k_max, n):
    coordinates = [Point(random.randint(1, n), random.randint(1, n)) for i in range(n)]
    for k in range(2, k_max):
        result = objective_function(k_means(coordinates, k, False))
        plt.scatter(k, result)
    plt.savefig('objective_function_result.png')


show_objective_function_plt(10, 100)

# результат находится в файле objective_function_result.png
# по полученному результату можно сказать, что наиболее подходящие значения 3 и 5.
# 3 - так как резкое уменьшение значения результирующей функции
# 5 - так как потом результирующая функия умменьшается медленно
