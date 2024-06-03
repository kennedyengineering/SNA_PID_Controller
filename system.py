# SNA PID Project
# system.py

# The system being controlled
class System:
    def __init__(self, y_k_start=0.45, y_k_coef=0.6, u_k_coef=0.01):
        # Initialize the system
        self.y_k = y_k_start
        self.y_k_coef = y_k_coef
        self.u_k_coef = u_k_coef

    def update(self, u_k):
        # Apply input and get new output of the system
        self.y_k = self.y_k_coef*self.y_k + self.u_k_coef*u_k
        return self.y_k

if __name__ == '__main__':
    pass
