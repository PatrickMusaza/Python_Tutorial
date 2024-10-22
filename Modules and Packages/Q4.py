from Geometry.Shapes import circle_area, circle_perimeter
from Geometry.Solids import cube_volume, cube_surface_area

radius = float(input("Enter the radius of the circle: "))
side = float(input("Enter the side of the cube: "))

print(f"Area of the circle: {circle_area(radius)}")
print(f"Perimeter of the circle: {circle_perimeter(radius)}")
print(f"Volume of the cube: {cube_volume(side)}")
print(f"Surface area of the cube: {cube_surface_area(side)}")
