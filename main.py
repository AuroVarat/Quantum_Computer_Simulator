from CircuitClass import QbitRegister
from CircuitClass import Gate as g

import numpy as np

input_file = np.genfromtxt('input.dat', delimiter=',', dtype=int)

# Pure State Network check the image in the folder
register = QbitRegister(input_file, name = "4PureNetwork") #initialise qbit register
h = g.hadamard(register,(1,)) # apply hadamard gate to qbit 1
p = g.phase_shift(h,(1,),2*np.pi) #apply phase shift to qbit 1
p = lambda phi: g.phase_shift(p,(1,),phi+np.pi/2) #apply phase shift to qbit 1


#EPR Paradox
register = QbitRegister([0,0], name ="4EPR") #initialise qbit register
h = g.hadamard(register,(1,)) # apply hadamard gate to qbit 1
cnot = g.cnot(h,[1,2]) #apply cnot gate with qbit 1 as target and 2 as control