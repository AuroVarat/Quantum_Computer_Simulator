
import numpy as np
from scipy.sparse import diags
# create a 2d array of 4x4 radom numbers
# this is the oracle matrix
oracle = np.random.rand(4,4)
#scipy sparse identity matrix
I = diags([1], [0], shape=(4, 4)).toarray()
print(oracle @ I )