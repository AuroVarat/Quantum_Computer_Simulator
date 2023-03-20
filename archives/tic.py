from lazyRegister import QbitRegister
import numpy as np
import inspect
import cProfile
import time
from scipy.sparse import diags,identity,eye,csr_matrix
from scipy.linalg import hadamard


isq2 = 1/np.sqrt(2) # 1/sqrt(2)isq2 = 1/np.sqrt(2) # 1/sqrt(2)


from tqdm import tqdm
from matplotlib import pyplot as plt


#take nqubits as input terminal
# import sys
# nqubits = int(sys.argv[1])

nqubits=9

x = np.array([1,0])
o = np.array([0,1])
b =np.array(([1,1])/np.sqrt(2))

def turn_to_basis(input_state):
    base = input_state[0]

    for i in range(1,len(input_state)):
      
        base =np.kron(base,input_state[i])
    return base

game_state = np.array([x,o,o,b,x,b,b,b,b])
fixed = np.where((game_state != b).any(axis=1))
state = turn_to_basis(game_state)

Q = QbitRegister(nqubits)
Q.set_state(state)
# for i in fixed[0]:

#     Q.hadamard(i+1)
print(np.where(Q.basisSpace != 0)[0].size)
# #%%
# dataset = np.genfromtxt('tic_dataset.txt',dtype=int)
# target = [1,0,1,2,2,2,1,0,1]

# oracle = diags(np.where(dataset == target, -1, 1))
# #oracle
# def grover_iterate(nqubits,n):
#     qc = QbitRegister(nqubits)

#     qc.addToCircuit(oracle)
#     qc.hadamard()
#     qc.mcz()  # multi-controlled-toffoli
#     qc.hadamard()
    
#     # We will return the diffuser as a gate
#     U_s = qc.to_gate()
#     U_s = qc.power(U_s,n)
#     # U_s.name = "U$_s$"
#     return U_s








# Q = QbitRegister(nqubits)
# Q.hadamard()

# Q.addToCircuit(grover_iterate(nqubits,Q.rotations))

# accuracy = np.amax(Q.measure().real)




# #%%
