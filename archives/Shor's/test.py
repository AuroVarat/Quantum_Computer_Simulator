from lazyRegister import QbitRegister
import numpy as np
from scipy.sparse import diags,eye,csr_matrix
#test what hadamard @ x do
import numpy as np

Q = QbitRegister(2)
Q.hadamard(1)
Q.hadamard(1)

print(Q.to_gate().toarray().real)
