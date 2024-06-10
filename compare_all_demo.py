# SNA PID Project
# compare_all_demo.py

import matplotlib.pyplot as plt

from system import System
from pid import PID
from sna_pid import SNA_PID_v1, SNA_PID_v2

controller0 = PID()
controller1 = SNA_PID_v1()
controller2 = SNA_PID_v2()

def run_simulation(controller):
    plant = System()

    time_steps = 300

    r_k = 1.0

    x = [0]
    y = [plant.y_k]
    s = [0]

    e = 0

    for i in range(time_steps):

        e += abs(r_k - y[-1])

        signal = controller.update(r_k, y[-1])

        x.append(i+1)
        y.append(plant.update(signal))
        s.append(signal)

    return x, y, s, e

x, y0, s0, e0 = run_simulation(controller0)
_, y1, s1, e1 = run_simulation(controller1)
_, y2, s2, e2 = run_simulation(controller2)

print("PID Total Error:", e0)
print("SNA PID v1 Total Error:", e1)
print("SNA PID v2 Total Error:", e2)

ax = plt.gca()
ax.set_xlim([0, 300])
ax.set_ylim([0, 1.1])

plt.plot(x, y0, label="Actual - PID")
plt.plot(x, y1, label="Actual - SNA PID v1")
plt.plot(x, y2, label="Actual - SNA PID v2")
plt.plot([0,300], [1.0, 1.0], label="Desired")
plt.ylabel('Fluid level')
plt.xlabel('Time units')
plt.title("PID Controller Comparison")
plt.legend()
plt.show()

plt.plot(x, s0, label="PID")
plt.plot(x, s1, label="SNA PID v1")
plt.plot(x, s2, label="SNA PID v2")
plt.ylabel('Flow rate')
plt.xlabel('Time units')
plt.title("PID Controller Comparison")
plt.legend()
plt.show()
