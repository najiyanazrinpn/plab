class Rectangle:
	__length = 0
	__width = 0
	def __init__(self,l,w):
		self.__length = l
		self.__width = w
	def area(self):
		return(self.__length*self.__width)
	def __lt__(self,o):
		return (self.area()<o.area())
l = int(input("Enter length of rectangle1: "))
w = int(input("Enter width of rectangle1: "))
r1 = Rectangle(l,w)
l = int(input("Enter length of rectangle2: "))
w = int(input("Enter width of rectangle2: "))
r2 = Rectangle(l,w)
if(r1<r2):
	print("Area of rectangle1 is less than area of rectangle2")
else:
	print("Area of rectangle2 is less than area of rectangle1")

