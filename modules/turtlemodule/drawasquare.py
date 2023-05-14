# Program to draw a square and fill color in it.

import turtle
import time

turtle.fillcolor('blue')
turtle.begin_fill()
for i in range(4):
    turtle.forward(250)
    turtle.right(90)
    time.sleep(1)
turtle.end_fill()
turtle.exitonclick()