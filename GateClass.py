
class Gate(LazyMatrix):
    def __init__(self):
        self.sm = SquareMatrix()
        self.smDim = 0
        self.qbpos = []

    def apply(self, v):
        w = Vector(self.dimension)
        for i in range(self.dimension):
            r = self.gather(i)
            i0 = i & ~self.scatter(r)
            for c in range(self.smDim):
                j = i0 | self.scatter(c)
                w[i] += self.sm[r, c] * v[j]
        return w

    def gather(self, i):
        j = 0
        for k in range(len(self.qbpos)):
            j |= ((i >> self.qbpos[k]) & 1) << k
        return j

    def scatter(self, j):
        i = 0
        for k in range(len(self.qbpos)):
            i |= ((j >> k) & 1) << self.qbpos[k]
        return i