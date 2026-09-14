class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point(14, 18)
print(point1.x)
point1.draw()

point2 = Point(10, 20)
print(point2.x)