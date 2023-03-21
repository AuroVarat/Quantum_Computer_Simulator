import numpy as np

import sys



sys.path.append("../resources")
sys.path.append("./resources")
from qCircuit import EagerCircuit,LazyCircuit
from scipy.sparse import diags
from tqdm import tqdm

# nqubits = int(sys.argv[1])
nqubits = 8

max_dataset_size = 2**nqubits
# only allow dataset size to be less than or equal to 2**nqbits. 
dataset_size = 2**nqubits
assert dataset_size <= max_dataset_size, "dataset size must be less than or equal to 2**nqbits"

def main():
    #CREATING AN ORACLE USING LAZY CIRCUIT CLASS
    qc = LazyCircuit(nqubits,"Oracle")
    qc.mcz([1,2,3,4,5,6],7)
    oracle = qc.to_gate()

  
    
    # dataset = np.arange(0,dataset_size)
    # target = np.random.randint(0,dataset_size)
    # oracle = diags(np.where(dataset == target, -1, 1))
    # target_index = np.where(dataset == target)[0][0]

    
    #%%
    circuit = EagerCircuit(nqubits,name ="Grover")
    circuit.h()
    circuit.set_oracle(oracle)
    # circuit.record_marked_state(target_index)

    for _ in tqdm(range(circuit.rotations)):
        circuit.oracle()
        circuit.h()
        circuit.reflect()
        circuit.h()
        # circuit.record_state_vector_projection()
        # circuit.record_marked_state(target_index)


    
    
    # circuit.visualise_state_history()
    # circuit.visualise_probability()
    # circuit.visualise_marked_state()

    circuit.measure()


    #%%

if __name__ == '__main__':

    main()
    # with open("groverEager.txt", "a") as f:
    #     f.write(str(nqubits)+",")
    #     f.write(','.join(map(str, circuit_output))+"\n")

  