import math
b = float(input("Base of triangle: "))
h = float(input("Height of triangle: "))
print(f"Area of the triangle: {0.5*b*h}")

num_sides = int(input("Number of sides of the polygon: "))
side_length = float(input("Length of a side: "))
area_polygon = (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))
print("Area of the Polygon:", area_polygon)