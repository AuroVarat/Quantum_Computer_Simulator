from lazyCircuit.lazyMatrix import QbitRegister
from lazyCircuit.qLazyGate import SingleQbitGate
import numpy as np
isq2 = 1/np.sqrt(2) # 1/sqrt(2)




q = QbitRegister(2)

q = SingleQbitGate.hadamard()(q)


print(np.where(q ==[1,0],[isq2, isq2],q))