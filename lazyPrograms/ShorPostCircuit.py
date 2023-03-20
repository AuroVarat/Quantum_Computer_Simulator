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

#make histogram of number of counts of states with probability > 0.01
df['state'][df['prob']>0.001].value_counts().plot(kind='bar')
#x axis label vertical
# the plot is cuttong off
plt.xticks(rotation=0)
plt.xlabel('State')
plt.ylabel('Counts')
plt.title('Shor Algorithm')
        
#save fig
plt.savefig('Shor.png')
