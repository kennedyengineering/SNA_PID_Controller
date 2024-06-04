# SNA PID Project
# sna_pid_v1_demo.py

import matplotlib.pyplot as plt

from system import System
from sna_pid import SNA_PID_v1

plant = System()
controller = SNA_PID_v1()

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
plt.title("Single Neuron Adaptive PID Controller v1")
plt.legend()
plt.show()
