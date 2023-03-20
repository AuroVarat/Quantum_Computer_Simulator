import os 

for i in range(1,14):
    os.system('python3 lazyPrograms/Grover.py {}'.format(int(i)))
    os.system('python3  eagerPrograms/Grover.py {}'.format(int(i)))