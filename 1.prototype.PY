
class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
         return f"Shape(x={self.x}, y={self.y}, color={self.color})"

class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def __clone__(self):
        return Circle(self.x, self.y, self.color, self.radius)

class Square(Shape):
    def __init__(self, x, y, color, side_length):
        super().__init__(x, y, color)
        self.side_length = side_length

    def __clone__(self):
         return Square(self.x, self.y, self.color, self.side_length)

# Usage
circle_prototype = Circle(10, 20, "red", 5)
square_prototype = Square(30, 40, "blue", 10)

circle1 = circle_prototype.__clone__() # Deep copy using __clone__()
square1 = square_prototype.__clone__()

circle1.move(5, 3)
square1.move(-2, 1)

print(circle_prototype) 
print(circle1) 
print(square_prototype) 
print(square1) 
