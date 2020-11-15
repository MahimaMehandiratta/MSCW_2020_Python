import turtle
nbrSides = int(input("Enter number of sides of the object: "))
for steps in range(nbrSides):
    turtle.forward(100)
    turtle.right(360/nbrSides)