import sys

from resources.qCircuit import LazyCircuit




circuit = LazyCircuit(4,name="Simple Circuit")
circuit.x(1)
circuit.h()
circuit.sequence()
circuit.measure()
