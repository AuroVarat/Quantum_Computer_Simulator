import numpy as np

import sys
sys.path.append("../resources")
from qCircuit import BasicCircuit
from scipy.sparse import diags
from tqdm import tqdm

nqubits = int(sys.argv[1])

max_dataset_size = 2**nqubits
# only allow dataset size to be less than or equal to 2**nqbits. 
dataset_size = 2**nqubits
assert dataset_size <= max_dataset_size, "dataset size must be less than or equal to 2**nqbits"

def main():
    
   
    dataset = np.arange(0,dataset_size)
    target = np.random.randint(0,dataset_size)
    oracle = diags(np.where(dataset == target, -1, 1))
    

       
    #%%
    circuit = BasicCircuit(nqubits,name = "GROVER")
    circuit.h()
    circuit.set_oracle(oracle,recorder=False)
    
    for _ in tqdm(range(circuit.rotations)):
        circuit.oracle()
        circuit.h()
        circuit.reflect()
        circuit.h()
        # circuit.record_state_vector_projection()
        


    
    
    # circuit.visualise_state_history()
    # circuit.visualise_probability()

    circuit.output()


    #%%

if __name__ == '__main__':

    main()

  