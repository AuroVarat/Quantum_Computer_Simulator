#%%
def test(n):
    for i in range(n):
        yield (0,1)
# %%
q = test(3)
print(next(q))

# %%
print(next(q))

#%%


for qubit in q:
    print(qubit)
# %%
