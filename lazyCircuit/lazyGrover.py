from lazyMatrix import QbitRegister

Q = QbitRegister(4)

for i in range(4):
    Q.hadamard()(i)

print(Q.output())