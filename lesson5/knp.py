from lesson2.functions import dist


# вспомогательная функция для поиска минимального расстояния
# между изолированной вершиной и уже входящей в состав дерева
def min_dist_find(current, points):
    min_dist = None
    next = None
    for point in points:
        if point == current:
            continue
        candidate_dist = dist(current.x, current.y, point.x, point.y)
        if min_dist is None or candidate_dist < min_dist:
            next = point
            min_dist = candidate_dist
    return next


# Поиск минимального расстояния в дереве (старт)
def find_start(points):
    min_distance = None
    start = None
    neighbour = None
    for point in points:
        candidate = min_dist_find(point, points)
        candidate_dist = dist(candidate.x, candidate.y, point.x, point.y)
        if min_distance is None or min_distance > candidate_dist:
            min_distance = candidate_dist
            start = point
            neighbour = candidate
    start.vertex_set.add(neighbour)
    neighbour.vertex_set.add(start)
    return start


# Создание минимального остовного дерева
def minimum_spanning_tree_creation(points):
    start = find_start(points)
    neighbour = next(iter(start.vertex_set))
    used_points = set()
    unused_points = set(points)

    used_points.add(start)
    used_points.add(neighbour)
    unused_points.remove(start)
    unused_points.remove(neighbour)

    for unused in unused_points:
        found_neighbour = min_dist_find(unused, used_points)
        unused.vertex_set.add(found_neighbour)
        found_neighbour.vertex_set.add(unused)
        used_points.add(unused)


# Удаление наибольших ребер
# Обход графа с помощью DFS
def delete_longer_edges(points, k):
    k -= 1
    distance_list = []
    used = set()
    for point in points:
        if used.__contains__(point):
            continue
        queue = [point]
        while len(queue) > 0:
            v = queue.pop(0)
            used.add(v)
            for vertex in v.vertex_set:
                if not used.__contains__(vertex):
                    distance_list.append(dist(v.x, v.y, vertex.x, vertex.y))
                    queue.append(vertex)
    distance_list.sort(reverse=True)
    for i in range(k):
        is_deleted = False
        for point in points:
            if is_deleted:
                break
            for neighbour in point.vertex_set:
                if dist(neighbour.x, neighbour.y, point.x, point.y) == distance_list[i]:
                    neighbour.vertex_set.remove(point)
                    point.vertex_set.remove(neighbour)
                    is_deleted = True
                    break
