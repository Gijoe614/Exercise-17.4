class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, self1):
        return Point(self.x + self1.x, self.y + self1.y)

    def increment(self, x, y):
        self.x += x
        self.y += y
        return self.x, self.y

points = Point(10, 15)
points1 = Point(7, 2)
points.increment(3, 6)
points2 = points + points1
print points2
