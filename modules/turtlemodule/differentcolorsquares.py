# Program to draw a pattern of different color squares with different angles.

import turtle

turtle.title("Different color squares")
turtle.bgcolor('black')
# for first square
turtle.color("red")
turtle.left(10)
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
    
# for second square
turtle.color("blue")
turtle.left(20)
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
    
# for third square
turtle.color("green")
turtle.left(30)
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
    
# for fourth square
turtle.color("orange")
turtle.left(40)
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
    
turtle.exitonclick()