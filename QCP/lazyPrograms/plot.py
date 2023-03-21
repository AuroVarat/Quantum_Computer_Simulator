#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


h = pd.read_csv("Shor.txt", sep=" ", header=None,dtype=str)
# %%
#count by h

h[0].value_counts().plot(kind="bar")
#rotate x label

plt.xlabel("Register State (Read from Top to Bottom, corresponding to Big-Endian)")
plt.ylabel("Counts")
plt.title("Shor's Algorithm | Measurement of State Counts")
#fig
plt.savefig("Shor.png",dpi=300)

# %%
