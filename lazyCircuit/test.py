from lazyRegister import QbitRegister
import numpy as np
from scipy.sparse import diags,eye,csr_matrix
#test what hadamard @ x do
import numpy as np

# Uqbits = 4
# def c_amod15(a,power):
#         if a not in [2,4,7,8,11,13]:
#             raise ValueError("'a' must be 2,4,7,8,11 or 13")
#         U = QbitRegister(Uqbits)
#         for _ in range(power):
#             if a in [2,13]:
#                 U.swap(3,4)
#                 U.swap(2,3)
#                 U.swap(1,2)
#             if a in [7,8]:
#                 U.swap(1,2)
#                 U.swap(2,3)
#                 U.swap(3,4)
#             if a in [4, 11]:
#                 U.swap(2,4)
#                 U.swap(1,3)
#             if a in [7,11,13]:
#                 U.x()
#         Us = U.to_gate()
       
#         cU = U.addControl(Us.toarray(),1)
#         return cU
# print(c_amod15(2,1).real.shape)
# print(np.ceil(2**(1/2)))
# # Q = QbitRegister(8)

# Q.addToCircuit(c_amod15(2,1))
n = 5
l = 4
a =eye(2**n,format="csr")
b = csr_matrix(np.random.rand(2**l,2**l))
print(a.shape)
print(b.shape)

a[2**l:,2**l:] = b



print(a.toarray())