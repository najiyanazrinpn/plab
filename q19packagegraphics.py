import graphics
from graphics import rectangle,circle
from graphics.threeD import sphere, cuboid
from graphics.circle import *

radius = int(input("Enter radius: "))
print("Area of circle: ",area_circle(radius))
print("Perimeter of circle: ",perimeter_circle(radius))
print("Area of sphere: ",sphere.area(radius))
print("Perimeter of sphere: ",sphere.perimeter(radius))

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
height = int(input("Enter height: "))
print("Area of rectangle: ",rectangle.area(length,breadth))
print("Perimeter of rectangle: ",rectangle.perimeter(length,breadth))
print("Area of cuboid: ", cuboid.area(length,breadth,height))
print("Perimeter of cuboid: ", cuboid.perimeter(length,breadth,height))