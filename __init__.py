import os

#take input from terminal
import sys
method = str(sys.argv[1])
assert method in ["lazy","eager"], "method must be either qiskit or qutip"
if method == 'lazy':
    program = str(sys.argv[2])
    assert program in ["Grover","Shor"], "Program must be either Grover, Shor"
    nqubits = int(sys.argv[3])
    
    # use os to run python file
    os.system("python3 {}Programs/{}.py {}".format(method,program,nqubits))
        
    
else:
    nqubits = int(sys.argv[3])
    print("Warning : For {} qubits Program can take very long time to run. Please be patient.".format(nqubits)) if nqubits > 13 else None
    
    os.system("python3 {}Programs/Grover.py {}".format(method,nqubits))
    


