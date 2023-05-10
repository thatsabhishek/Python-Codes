# Program to form any Algebric Equation using numpy.

import matplotlib.pyplot as p
import numpy as n

x = n.arange(1,11)
y = 2*x**3 + 5*x**2 + 4*x + 3
p.plot(x, y)
p.title("Algebra Graph for equation 2x^3+5x^2+4x+3.")
p.show()