import random

import matplotlib.pyplot as plt

from lesson5.domain import Point
from lesson5.knp import minimum_spanning_tree_creation, delete_longer_edges

color_map = {
    0: 'r',
    1: 'b',
    2: 'g',
    3: 'y',
    4: 'm',
    5: 'c'
}

n = 5
points = [Point(random.randint(1, 50), random.randint(1, 50)) for i in range(n)]


# визуализация дерева
def show_minimum_spanning_tree(points, save):
    used = set()
    x = []
    y = []

    stack = [points[0]]
    while len(stack) > 0:
        v = stack.pop(len(stack) - 1)
        if used.__contains__(v):
            continue
        used.add(v)
        for vertex in v.vertex_set:
            if used.__contains__(vertex):
                continue
            x.append(v.x)
            y.append(v.y)
            x.append(vertex.x)
            y.append(vertex.y)
            stack.append(vertex)
    plt.plot(x, y, color="blue", marker="o")
    if save:
        plt.savefig("tree.demonstration")
    plt.show()


# визуализация распределения по кластерам:
# поиск компонент связности и обход с помощью DFS
def show_graphs(points, save):
    cluster = -1
    used = set()
    for point in points:
        if used.__contains__(point):
            continue
        cluster += 1
        color = color_map[cluster]
        queue = [point]
        while len(queue) > 0:
            v = queue.pop(0)
            plt.scatter(v.x, v.y, color=color)
            used.add(v)
            for vertex in v.vertex_set:
                if not used.__contains__(vertex):
                    plt.scatter(vertex.x, vertex.y, color=color)
                    queue.append(vertex)
    if save:
        plt.savefig("clustering_result.png")
    plt.show()


minimum_spanning_tree_creation(points)
show_minimum_spanning_tree(points, True)
delete_longer_edges(points, 3)
show_graphs(points, True)
