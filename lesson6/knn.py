from functools import cmp_to_key

from lesson2.functions import dist
from lesson6.domain import ClassifierKnn


def sort_classifier_data(data):
    return sorted(data, key=cmp_to_key(ClassifierKnn.comparator))


def knn(clusters, test_data, k, clusters_count):
    for point in test_data:
        distance_list = []
        for cluster in clusters:
            for cluster_element in cluster.elements:
                distance_list.append(
                    ClassifierKnn(
                        cluster.number,
                        dist(point.x, point.y, cluster_element.x, cluster_element.y)
                    )
                )
        sorted_distance_list = sort_classifier_data(distance_list)
        k_minimal_distance_list = sorted_distance_list[0:k]
        cluster_counter = [0 for i in range(clusters_count)]
        for classifier in k_minimal_distance_list:
            cluster_counter[classifier.cluster] += 1
        max_cluster_hit = 0
        counter = 0
        for i in range(clusters_count):
            if cluster_counter[i] > counter:
                counter = cluster_counter[i]
                max_cluster_hit = i
        point.cluster = max_cluster_hit
