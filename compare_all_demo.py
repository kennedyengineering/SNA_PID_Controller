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
    for i in range(time_steps):

        signal = controller.update(r_k, y[-1])

        x.append(i+1)
        y.append(plant.update(signal))

    return x, y

x, y0 = run_simulation(controller0)
_, y1 = run_simulation(controller1)
_, y2 = run_simulation(controller2)

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
