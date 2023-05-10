# A simple program to draw a line chart with labels and title

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Square Values")
plt.plot(x, y)
plt.show()