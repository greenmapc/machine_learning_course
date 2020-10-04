from lesson2.domain import Point
import random

from lesson2.k_means import k_means

n, k = 100, 5
coordinates = [Point(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]

k_means(coordinates, k)
