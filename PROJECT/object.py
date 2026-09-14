import turtle

class Polygon:
    def __init__(self, sides, name, size=100, color="black", line_thickness=2):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2)*180
        self.angle = self.interior_angles / self.sides
        pass
    def Draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180 - self.angle)

# This makes class square inherit properties from class polygon
class Square(Polygon):
    def __init__(self, sides, name, size=100, color="black", line_thickness=2):
        super().__init__(4, name, size, color, line_thickness)

    def Draw(self):
        turtle.fillcolor("blue")
        turtle.begin_fill()
        super().Draw()
        turtle.end_fill()


square = Square(4, "Square", 300, color="blue")
pentagon = Polygon(5, "Pentagon")
hexagon = Polygon(6, "Hexagon", 300, color="blue", line_thickness=11)

print(square.sides)
print(square.name)
print(square.interior_angles)
print(square.angle)

print(pentagon.sides)
print(pentagon.name)

square.Draw()
turtle.done()

# pentagon.Draw()

# hexagon.Draw()