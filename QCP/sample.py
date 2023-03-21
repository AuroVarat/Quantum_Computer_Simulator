"""
Flip a coin?

This is a sample file to test the qCircuit modules. Feel Free to play around with building your own circuits."""
import sys
sys.path.append("../resources")
sys.path.append("./resources")
import numpy as np
from resources.qCircuit import LazyCircuit,EagerCircuit
from resources.qComponents import ReusableComponents as rc

n = 1

circuit = EagerCircuit(n,name="Simple Circuit")

circuit.h()



circuit.measure()

circuit.output()
