from CircuitClass import Gate, QubitRegister
import numpy as np

input_file = np.genfromtxt('input.dat', delimiter=',', dtype=int)

#Initialise a 3 qubit register

register = QubitRegister(input_file)

# Apply hadamard on the first qubit
print(register[0]@Gate(2).hadamard)
print(register[0]@Gate(2).phase_shift(2*np.pi))

