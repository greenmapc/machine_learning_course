import numpy as np

from lesson2.functions import dist
from lesson3.domain import Point


def calculate_centers(k, m, points):
    result = []
    for i in range(0, k):
        numerator_x = 0
        numerator_y = 0
        denominator_x = 0
        denominator_y = 0

        for point in points:
            numerator_x += pow(point.cluster_membership_probability[i], m) * point.x
            denominator_x += pow(point.cluster_membership_probability[i], m)

            numerator_y += pow(point.cluster_membership_probability[i], m) * point.y
            denominator_y += pow(point.cluster_membership_probability[i], m)

        x_cluster_center = numerator_x / denominator_x
        y_cluster_center = numerator_y / denominator_y

        result.append(Point(x_cluster_center, y_cluster_center))

    return result


# расчет коэффициента принадлежности к определенному кластеру
def membership_coefficient(cluster_num, centers, point, m):
    result = 0
    distance_for_cluster = dist(centers[cluster_num].x, centers[cluster_num].y, point.x, point.y)
    for center in centers:
        result += pow(distance_for_cluster / dist(center.x, center.y, point.x, point.y), 2 / (1 - m))
    return result


# нормализация коэффициента - чтобы сумма стала < 1 (т.е. перевод в вероятность попадания элемента в кластер)
def normalize_coefficient(cluster_membership_probability):
    sum = 0
    for probability in cluster_membership_probability:
        sum += probability
    for i in range(0, len(cluster_membership_probability)):
        cluster_membership_probability[i] /= sum


# решающая функция
def calculate_decision_function(points, centers):
    function_result = 0
    for point in points:
        probability = point.cluster_membership_probability
        for i in range(0, len(probability)):
            function_result += probability[i] * dist(point.x, point.y, centers[i].x, centers[i].y)
    return function_result


# инициализация центроидов, можно было бы выбрать случайные
def init_centroid(points, k, x_center, y_center):
    R = 0
    n = len(points)
    for i in range(0, n):
        r = dist(x_center, y_center, points[i].x, points[i].y)
        if r > R:
            R = r
    x_cc = [R * np.cos(2 * np.pi * i / k) + x_center for i in range(k)]
    y_cc = [R * np.sin(2 * np.pi * i / k) + y_center for i in range(k)]
    result = []
    for i in range(0, k):
        result.append(Point(x_cc[i], y_cc[i]))
    return result


def init_cluster_membership(points, k):
    for point in points:
        for i in range(0, k):
            point.cluster_membership_probability.append(0)


EPSILON = 0.2


# m - коэффициент неопределенности
# k - количество кластеров
def c_means(points, m, k):
    first_iteration = True
    init_cluster_membership(points, k)

    x_center = np.mean(list(map(lambda e: e.x, points)))
    y_center = np.mean(list(map(lambda e: e.y, points)))

    current_decision = 1
    previous_decision = 0

    while abs(previous_decision - current_decision) > EPSILON:
        previous_decision = current_decision
        if first_iteration:
            centers = init_centroid(points, k, x_center, y_center)
            first_iteration = False
        else:
            centers = calculate_centers(k, m, points)
        for point in points:
            for i in range(0, len(centers)):
                point.cluster_membership_probability[i] = membership_coefficient(i, centers, point, m)
            normalize_coefficient(point.cluster_membership_probability)
        current_decision = calculate_decision_function(points, centers)
