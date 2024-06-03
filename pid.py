# SNA PID Project
# pid.py

import numpy as np

# The incremental PID controller
class PID:
    def __init__(self, Kp=30, Ki=5, Kd=0.00001):
        # Initialize the system
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.e_k = np.zeros(3)  # e_k[0] is current (k), e_k[1] is last timestep (k-1), e_k[2] is timestep before that (k-2)
        self.u_k = 0
        
    def update(self, r_k, y_k):
        # Compute error and get new output of the controller
        self.e_k[1:] = self.e_k[:-1]; self.e_k[0] = r_k - y_k

        self.u_k = self.u_k + \
              self.Kp*(self.e_k[0] - self.e_k[1]) + \
              self.Ki*(self.e_k[0]) + \
              self.Kd*(self.e_k[0] - 2*self.e_k[1] + self.e_k[2])
        
        return self.u_k
    
if __name__ == '__main__':
    pass
