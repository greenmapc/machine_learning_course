class Cluster:
    def __init__(self, elements, number, color, x_center=None, y_center=None):
        self.last_x_center = None
        self.last_y_center = None
        self.x_center = x_center
        self.y_center = y_center
        self.number = number
        self.elements = elements
        self.color = color

    def add_element(self, point):
        self.elements.append(point)

    def clean_elements(self):
        self.elements.clear()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
