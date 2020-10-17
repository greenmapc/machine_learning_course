class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.noise = False
        self.visited = False
        self.cluster = None
