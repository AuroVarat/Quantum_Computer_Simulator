import sys

from resources.qCircuit import LazyCircuit




circuit = LazyCircuit(2,name="Simple Circuit")
circuit.x()
circuit.h(1)
# circuit.sequence()
circuit.measure()
