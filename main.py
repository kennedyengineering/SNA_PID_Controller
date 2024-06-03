# SNA PID Project
# main.py

import matplotlib.pyplot as plt

from system import System
from pid import PID

plant = System()
controller = PID()

time_steps = 300

r_k = 1.0

x = [0]
y = [plant.y_k]
for i in range(time_steps):

    signal = controller.update(r_k, y[-1])

    x.append(i+1)
    y.append(plant.update(signal))

ax = plt.gca()
ax.set_xlim([0, 300])
ax.set_ylim([0, 1.1])

plt.plot(x, y, label="Actual")
plt.plot([0,300], [r_k, r_k], label="Desired")
plt.ylabel('Fluid level')
plt.xlabel('Time units')
plt.title("Zeigler-Nichols Tuned PID Controller")
plt.legend()
plt.show()
