# Program to draw a differnt colored circle on a black background.

import turtle
import random
turtle.bgcolor("black")
colors = ['red','blue','light blue','green','yellow','pink','orange','purple']
turtle.pensize(2)
turtle.speed(5)
for angle in range(0, 360, 20):
    turtle.color(random.choice(colors))
    turtle.seth(angle)
    turtle.circle(100)
    
turtle.exitonclick()