# Single Neuron Adaptive PID Controller
### CSC 509 Final Project, Braedan Kennedy (bkenne07@calpoly.edu)

## Installation
1. Create a new virtual environment `python3 -m venv venv`
2. Activate virtual environment `source venv/bin/activate`
3. Install dependencies `pip3 install -r requirements.txt`

## Algorithms
### Incremental PID
Your regular PID algorithm, tuned using the Ziegler-Nichols method

### Single Neuron Adaptive PID v1
A SNA-PID algorithm implementation featuring:
1. Weight normalization
2. d(y_k)/d(u_k) approximation via u_k

### Single Neuron Adaptive PID v2
A SNA-PID algorithm implementation extending v1 to include:
1. 2*e_k[0] - e_k[1] input term

## Running Demos
### Incremental PID Demo
`python3 pid_demo.py`

See the standard PID algorithm home in on a stationary setpoint
### Single Neuron Adaptive PID v1 Demo
`python3 sna_pid_demo_v1.py`

See the SNA-PID v1 algorithm home in on a stationary setpoint
### Single Neuron Adaptive PID v2 Demo
`python3 sna_pid_demo_v2.py`

See the SNA-PID v2 algorithm home in on a stationary setpoint
### Compare All Demo
`python3 compare_all_demo.py`

See all the PID algorithms home in on a stationary setpoint
### Compare All Dynamic Demo
`python3 compare_all_dynamic_demo.py`

See all the PID algorithms home in on a moving setpoint


Halfway through the simulation the plant dynamics change allowing the adaptive nature of SNA-PID to be visualized

## Results
