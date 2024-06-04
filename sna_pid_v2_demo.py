# SNA PID Project
# sna_pid_v2_demo.py

import matplotlib.pyplot as plt

from system import System
from sna_pid import SNA_PID_v2

plant = System()
controller = SNA_PID_v2()

time_steps = 300

r_k = 1.0

x = [0]
y = [plant.y_k]
s = [0]

e = 0

for i in range(time_steps):

    e += r_k - y[-1]

    signal = controller.update(r_k, y[-1])

    x.append(i+1)
    y.append(plant.update(signal))
    s.append(signal)

print("SNA PID v2 Total Error:", e)

ax = plt.gca()
ax.set_xlim([0, 300])
ax.set_ylim([0, 1.1])

plt.plot(x, y, label="Actual")
plt.plot([0,300], [r_k, r_k], label="Desired")
plt.ylabel('Fluid level')
plt.xlabel('Time units')
plt.title("Single Neuron Adaptive PID Controller v2")
plt.legend()
plt.show()

plt.plot(x, s)
plt.ylabel('Flow rate')
plt.xlabel('Time units')
plt.title("Single Neuron Adaptive PID Controller v2")
plt.show()
