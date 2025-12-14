# polymorphism_demo.py
import math

# Base Class
class Shape:
    def area(self):
        """Calculate the area of the shape. Must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate rectangle's area."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Override area method to calculate circle's area."""
        return math.pi * (self.radius ** 2)
