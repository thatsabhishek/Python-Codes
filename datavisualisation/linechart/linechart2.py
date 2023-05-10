# Program to form 2 lines on a line chart with label and legend.

import matplotlib.pyplot as plt

x1 = [1,4,7,10,13,16]
y1 = [5,9,13,17,21,25]
plt.plot(x1, y1, label = "First Line")

x2 = [3,9,12,15]
y2 = [5,15,20,30]
plt.plot(x2, y2, label = "Second Line")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line Graph")
plt.legend()
plt.show()