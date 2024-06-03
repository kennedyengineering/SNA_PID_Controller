# SNA PID Project
# main.py

import matplotlib.pyplot as plt

from system import System

plant = System()

time_steps = 300

x = [0]
y = [plant.y_k]
for i in range(time_steps):
    x.append(i+1)
    y.append(plant.update(0))

plt.plot(x, y)
plt.show()
