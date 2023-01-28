from ComponentClass import QbitRegister

import numpy as np

# input_file = np.genfromtxt('input.dat', delimiter=',', dtype=int)

# # Pure State Network check the image in the folder
register = QbitRegister(2, name = "4PureNetwork") #initialise qbit register
register.hadamard(0) # apply hadamard gate to qbit 1
register.phase_shift(0,2*np.pi) #apply phase shift to qbit 1
lambda theta : register.phase_shift(0,theta) #apply phase shift to qbit 1

#EPR Paradox/ uncomment below to run
# register = QbitRegister(2, name ="4EPR") #initialise qbit register
# register.hadamard(0) # apply hadamard gate to qbit 1
# register.cnot(0) #apply cnot gate with qbit 1,2 as control and target respectively
# print(register)