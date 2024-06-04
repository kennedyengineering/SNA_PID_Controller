# SNA PID Project
# compare_all_demo_dynamic.py

import matplotlib.pyplot as plt
import numpy as np

from system import System
from pid import PID
from sna_pid import SNA_PID_v1, SNA_PID_v2

controller0 = PID()
controller1 = SNA_PID_v1(K=20)      # Double controller gain to counter system cutting controller contribution in half
controller2 = SNA_PID_v2(K=20)

def run_simulation(controller):
    plant = System()

    time_steps = 600

    x = [0]
    y = [plant.y_k]
    s = [0]
    r = [1]

    e = 0

    for i in range(time_steps):

        if i == time_steps/2:
            # Cut controller contribution in half
            plant.u_k_coef = 0.005

        e += r[-1] - y[-1]

        signal = controller.update(r[-1], y[-1])

        x.append(i+1)
        y.append(plant.update(signal))
        s.append(signal)
        r.append(0.1*np.sin(x[-1]/10) + 1)

    return x, y, s, r, e

x, y0, s0, r, e0 = run_simulation(controller0)
_, y1, s1, _, e1 = run_simulation(controller1)
_, y2, s2, _, e2 = run_simulation(controller2)


print("PID Total Error:", e0)
print("SNA PID v1 Total Error:", e1)
print("SNA PID v2 Total Error:", e2)

plt.plot(x, y0, label="Actual - PID")
plt.plot(x, y1, label="Actual - SNA PID v1")
plt.plot(x, y2, label="Actual - SNA PID v2")
plt.plot(x, r, label="Desired")
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
