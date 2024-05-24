class LegacyRectangle:
  """Legacy class representing a rectangle with incompatible methods."""
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)


class ModernShape:
  def get_area(self):
    pass


class RectangleAdapter(ModernShape):
    def __init__(self, legacy_rectangle):
        self.legacy_rectangle = legacy_rectangle
    def get_area(self):
        return self.legacy_rectangle.get_area()

# Usage
legacy_rectangle = LegacyRectangle(5, 3)

# Using legacy methods
print(legacy_rectangle.get_area())  # Output: 15
print(legacy_rectangle.get_perimeter())  # Output: 16

# Adapting to ModernShape interface
modern_shape = RectangleAdapter(legacy_rectangle)

# Using the modern interface method
print(modern_shape.get_area())  # Output: 15 (using the adapter)