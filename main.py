from ComponentClass import QbitRegister
import numpy as np

# input_file = np.genfromtxt('input.dat', delimiter=',', dtype=int)

# Pure State Network check the image in the folder
register = QbitRegister(3, name = "SampleHadamardOperation") #initialise qbit register
register.hadamard(1) # apply hadamard gate to qbit 1
register.hadamard(2) # apply hadamard gate to qbit 2
register.hadamard(3) # apply hadamard gate to qbit 3
register.output()



# # Pure State Network check the image in the folder
register = QbitRegister(3, name = "4PureNetwork") #initialise qbit register
register.hadamard(1) # apply hadamard gate to qbit 1
register.phase_shift(1,2*np.pi) #apply phase shift to qbit 1
register.phase_shift(1,phi=0) #apply phase shift to qbit 1
register.output()



#Implementation of 2 qbit EPR Paradox
register = QbitRegister(2, name ="4EPR") #initialise qbit register
register.hadamard(0) # apply hadamard gate to qbit 1
register.cnot(0) #apply cnot gate with qbit 1,2 as control and target respectively
register.output()  