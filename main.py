import numpy as np
from circuitElements.qRegister import QbitRegister


# Simple Grover's Algorithm
register = QbitRegister(3, name = "SampleHadamardOperation") #initialise qbit register
register.hadamard() # apply hadamard gate to register 
register.oracle(winner=4) # apply oracle gate to qbit 1 and 2
register.hadamard() # apply hadamard gate to the register
register.control_phase_shift(except_state=1,phi=np.pi) #apply phase shift to qbit 2
register.hadamard() # apply hadamard gate to qbit 1


register.output()
