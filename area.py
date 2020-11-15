import math

#AREA OF CIRCLE
radius = float(input("Enter the radius of the circle:"))
area_circle = math.pi*pow(radius,2)
print("Area of the circle is {0:.2f}".format(area_circle) +" square units")

#AREA OF SQUARE
side = float(input("Enter the side of the square:"))
area_square = pow(side,2)
print("Area of the square is {0:.2f}".format(area_square) +" square units")

#AREA OF RECTANGLE
length = float(input("Enter the length of the rectangle:"))
breadth = float(input("Enter the breadth of the rectangle:"))
area_rectangle = length*breadth
print("Area of the rectangle is {0:.2f}".format(area_rectangle) +" square units")