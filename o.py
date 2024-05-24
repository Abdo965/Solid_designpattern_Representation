# Example demonstrating Open/Closed Principle

# Abstract class defining the shape interface
class Shape:
    def area(self):
        pass

# Rectangle class implementing the shape interface
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle class implementing the shape interface
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# AreaCalculator class responsible for calculating the total area of shapes
class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area

# Usage
if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    circle = Circle(3)

    # Creating a list of shapes
    shapes = [rectangle, circle]

    # Calculating the total area of shapes
    calculator = AreaCalculator()
    total_area = calculator.calculate_area(shapes)
    print("Total area of shapes:", total_area)
