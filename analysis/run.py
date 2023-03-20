import os 

for i in range(1,14):
    os.system('python3 lazyCircuit/lazyGrover.py {}'.format(int(i)))
    os.system('python3  basisCircuit/grover.py {}'.format(int(i)))