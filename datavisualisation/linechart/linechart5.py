#  Program to draw line chart of sin() & cos(x)

import matplotlib.pyplot as p
import numpy as n

x = n.arange(0., 15, 0.1)
a = n.sin(x)
b = n.cos(x)
p.plot(x, a, label = "sin(x)")
p.plot(x, b, label = "cos(x)")
p.legend()
p.title("Graph of sin(x) & cos(x)")
p.show()