import random

from lesson3.c_means import c_means
from lesson3.domain import Point

n, k = 15, 3
points = [Point(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]

c_means(points, 1.5, k)

for point in points:
    print(str(point.x) + ":" + str(point.y), end=" ")
    print(point.cluster_membership_probability)
