from lesson2.functions import dist


def dbscan(points, eps, m):
    cluster = 0
    for p in points:
        if p.visited:
            continue
        p.visited = True
        neighbors = find_neighbors(p, points, eps)
        if len(neighbors) < m:
            p.noise = True
            continue
        cluster += 1
        cluster_expand(p, neighbors, cluster, points, eps, m)


def cluster_expand(point, neighbors, cluster, points, eps, m):
    point.cluster = cluster
    for candidate in neighbors:
        if not candidate.visited:
            candidate.visited = True
            candidate_neighbors = find_neighbors(candidate, points, eps)
            if len(candidate_neighbors) >= m:
                neighbors = neighbors.union(candidate_neighbors)
        if candidate.cluster is None:
            candidate.cluster = cluster


def find_neighbors(point, points, eps):
    result = set()
    for candidate in points:
        if dist(point.x, point.y, candidate.x, candidate.y) <= eps:
            result.add(candidate)
    return result


def noise_distribution(points):
    for noise in points:
        if noise.noise:
            noise.noise = False
            min_dist = 1000
            for point in points:
                if not point.noise:
                    current_min = dist(noise.x, noise.y, point.x, point.y)
                    if point != noise and min_dist > current_min:
                        noise.cluster = point.cluster
                        min_dist = current_min
