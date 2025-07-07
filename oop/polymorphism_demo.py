# polymorphism_demo.py
import math

class Shape:
    """Base class representing a geometric shape."""
    
    def area(self):
        """Calculate the area of the shape.
        
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """A rectangle shape defined by length and width."""
    
    def __init__(self, length, width):
        """
        Initialize a rectangle.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle (length × width)."""
        return self.length * self.width


class Circle(Shape):
    """A circle shape defined by its radius."""
    
    def __init__(self, radius):
        """
        Initialize a circle.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle (π × radius²)."""
        return math.pi * (self.radius ** 2)