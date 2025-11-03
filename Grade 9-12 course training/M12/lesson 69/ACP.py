import math

class Polygon:
    def __init__(self, sides, length):
        """
        sides: number of sides (integer, >= 3)
        length: side length (float or int)
        """
        if sides < 3:
            raise ValueError("Polygon must have at least 3 sides.")
        self.sides = sides
        self.length = length

    def perimeter(self):
        return self.sides * self.length

    def interior_angle(self):
        # Each interior angle in a regular polygon
        return (self.sides - 2) * 180 / self.sides

    def area(self):
        # Area of a regular polygon using formula:
        # (n * s^2) / (4 * tan(pi/n))
        return (self.sides * self.length**2) / (4 * math.tan(math.pi / self.sides))

    def __str__(self):
        return (f"Polygon with {self.sides} sides of length {self.length}\n"
                f"Perimeter: {self.perimeter()}\n"
                f"Interior Angle: {self.interior_angle():.2f}°\n"
                f"Area: {self.area():.2f}")


# Example Usage
if __name__ == "__main__":
    n = int(input("Enter number of sides: "))
    s = float(input("Enter side length: "))

    polygon = Polygon(n, s)
    print(polygon)
