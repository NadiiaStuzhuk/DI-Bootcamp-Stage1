# Instructions
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.



# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.


# Bonus Challenge (Optional)
# If you want an extra challenge:

# Install the Turtle module (pip install PythonTurtle)
# Draw the sorted circles visually on the screen!


# 💡 Tip:

# Test your implementation by creating several circles and printing comparisons, additions, and sorted results.

import math

class Circle:
    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    
    @classmethod
    def from_diameter(cls, diameter):
        """Allows creating a Circle object via a diameter: c = Circle.from_diameter(10)"""
        return cls(radius=diameter / 2)

    @property
    def diameter(self):
        """Queries the diameter of the circle."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Allows the user to modify the diameter directly."""
        self.radius = value / 2

    @property
    def area(self):
        """Computes and returns the circle's area (pi * r^2)."""
        return math.pi * (self.radius ** 2)



    def __str__(self):
        """Prints user-friendly attributes of the circle."""
        return f"Circle(Radius: {self.radius:.2f}, Diameter: {self.diameter:.2f})"

    def __repr__(self):
        """Official object representation."""
        return f"Circle({self.radius})"

    def __add__(self, other):
        """Adds two circles together and returns a new Circle with the combined radius."""
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)


    def __eq__(self, other):
        """Checks if two circles are equal in size."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        """Less-than comparison. Required for Python's built-in sort() functionality."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other):
        """Greater-than comparison."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius





c1 = Circle(4)                 
c2 = Circle.from_diameter(10) 
c3 = Circle(2)                

print("--- 1. String Representations & Property Queries ---")
print(c1)
print(f"c2 Radius: {c2.radius} | c2 Diameter: {c2.diameter} | c2 Area: {c2.area:.2f}")

print("\n--- 2. Addition (c1 + c3) ---")
c4 = c1 + c3
print(f"New circle from adding c1 and c3: {c4}")

print("\n--- 3. Comparisons ---")
print(f"Is c1 bigger than c2? {c1 > c2}")  
print(f"Is c2 bigger than c3? {c2 > c3}") 
print(f"Is c1 equal to a new Circle(4)? {c1 == Circle(4)}") # True

print("\n--- 4. Storing & Sorting a List of Circles ---")
circle_list = [c1, c2, c3, c4]
print("Original list:", circle_list)


circle_list.sort()
print("Sorted list (smallest to largest):", circle_list)