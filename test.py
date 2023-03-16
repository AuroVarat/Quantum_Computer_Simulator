import numpy as np


print(1/np.sqrt(2)) # 1/sqrt(2))
possible = [0,1,1/np.sqrt(2)] # 1/sqrt(2)]
# np choice
b =np.random.choice(possible,(500,9))
b = np.unique(b,axis=0)
# create unique arrays of random numbers 
while b.shape[0] < 500:
    a = np.random.choice(possible,(500-b.shape[0],9))
    b = np.concatenate((b,a),axis=0)
    b = np.unique(b,axis=0)

print(b.shape)
#numpy save b
np.savetxt("b.txt",b)