class Point:
    def __init__(self, x, y, cluster=None):
        self.x = x
        self.y = y
        self.cluster = cluster


class ClassifierKnn:
    def __init__(self, cluster, distance):
        self.cluster = cluster
        self.distance = distance

    def comparator(x, y):
        if x.distance < y.distance:
            return -1
        elif x.distance > y.distance:
            return 1
        else:
            return 0
