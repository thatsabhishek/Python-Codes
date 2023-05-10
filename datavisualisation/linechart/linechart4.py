# Program to draw different line styles with different colors.

import matplotlib.pyplot as p
import numpy as n

a = n.arange(1,20)
p.plot(a,'r', ls = '--') # dashed line
p.plot(a+1,'y', ls = '-.') # dashdotted line 
p.plot(a+2,'b', ls = '-') # solid line
p.plot(a+3,'g', ls = ':') # dotted line
p.show()