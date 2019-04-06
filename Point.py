class Point:
    id = 0
    x = 0
    y = 0

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def calculateDistance(Point a, Point b):
        distance = (((a.x - b.x) ** 2) + ((a.y - b.y) ** 2)) ** 0.5
        return distance
