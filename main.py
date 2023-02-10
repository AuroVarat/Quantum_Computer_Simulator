#%%
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm

#%%
# Simple Grover's Algorithm #ha
register = QbitRegister(11, name = "SampleHadamardOperation") #initialise qbit register

def grover_iterate():
    register.hadamard() # apply hadamard gate to register 
    register.oracle(winner=4) # apply oracle gate to qbit 1 and 2
    register.hadamard() # apply hadamard gate to the register
    register.control_phase_shift(except_state=1,phi=np.pi) #apply phase shift to qbit 2
    register.hadamard() # apply hadamard gate to qbit 1

for i in tqdm(range(1)):
    grover_iterate()
#%%
np.max(register.output())
#%%
register.visualise()
