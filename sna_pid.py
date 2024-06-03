# SNA PID Project
# sna_pid.py

import numpy as np

# The Single Neuron Adaptive PID controller
# v0: sgn function approximation
class SNA_PID_v0:
    def __init__(self, K=50, LRp=0.6, LRi=0.7, LRd=0.4):
        # Initialize the system
        self.K = K

        self.lr = np.array([LRp, LRi, LRd])
        self.w_k = np.ones(3)
        self.e_k = np.zeros(3)  # e_k[0] is current (k), e_k[1] is last timestep (k-1), e_k[2] is timestep before that (k-2)
        self.u_k = 0

        self.s_k = np.zeros(2)
        self.y_k = np.zeros(2)
        
    def update(self, r_k, y_k):
        # Compute error
        self.e_k[1:] = self.e_k[:-1]; self.e_k[0] = r_k - y_k

        # Define input terms
        x = np.array([self.e_k[0] - self.e_k[1], 
                      self.e_k[0], 
                      self.e_k[0] - 2*self.e_k[1] + self.e_k[2]])

        # Normalize weights
        w_k_norm = self.w_k / np.sum(np.abs(self.w_k))

        # Compute change in controller output
        self.s_k[1:] = self.s_k[:-1]; self.s_k[0] = self.K * np.sum(w_k_norm * x)

        # Compute controller output
        self.u_k = self.u_k + self.s_k[0]

        # Approximate d(y_k)/d(s_k)
        self.y_k[1:] = self.y_k[:-1]; self.y_k[0] = y_k
        approx = np.sign((self.y_k[0] - self.y_k[1])/(self.s_k[0] - self.s_k[1]))

        # Update weights
        self.w_k = self.w_k + self.lr*self.K*self.e_k[0]*approx*x

        # Return controller output
        return self.u_k

# The Single Neuron Adaptive PID controller
# v1: u_k approximation
class SNA_PID_v1:
    pass

# The Single Neuron Adaptive PID controller
# v2: 2*e_k[0] - e_k[1] input term
class SNA_PID_v2:
    pass
    
if __name__ == '__main__':
    pass
