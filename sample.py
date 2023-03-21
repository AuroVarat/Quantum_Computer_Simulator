#play around to create your own circuit if you would like
import sys


from resources.qCircuit import LazyCircuit
from resources.qComponents import reusableComponents as rc



circuit = LazyCircuit(12,name="Simple Circuit")
qft = rc.qft_dagger(8)
print(qft.shape)
circuit.addToCircuit(qft,ith_qbit=1,name="QFT")
circuit.sequence()
circuit.measure()
