import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
prob = np.genfromtxt('Shor.txt', delimiter=',',dtype=str)

state = prob[:,0]
prob = prob[:,1].astype(float)

# #print first 10 states and their probabilities
# for   i in range(10):
#     print(state[i],prob[i])
    
# # #trim last 4 characters of state
# state = [x[:-4] for x in state]

#trim first 2 characters of state
state = [x[4:] for x in state]
# make pandas column with state and probability
df = pd.DataFrame({'state':state,'prob':prob})


#probability of the first 15 state plot
plt.figure(figsize=(10,5))
plt.bar(df['state'][:15],df['prob'][:15])
plt.xlabel('state')
plt.ylabel('probability')
plt.title('probability of the first 15 state')
plt.savefig('Shor.png')