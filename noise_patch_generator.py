import numpy as np
import random as rd


class NoisePatchGenerator():
    def __init__(self, size):
        self.size = size
        self.r = size*8.4/40
        self.rand_move = size//2+self.r
        self.ones_batch = []

    def add_contrast(self, x, exp=0.5, dropout=0.7):
        return x ** (1+exp) * dropout

    def one_patch(self):
        out = np.zeros((self.size, self.size))
        targ_x = (self.size-1)/2 + (0.5-rd.random())*2*self.rand_move
        targ_y = (self.size-1)/2 + (0.5-rd.random())*2*self.rand_move
        for i2 in range(self.size):
            for j2 in range(self.size):
                if (i2-targ_x)**2+(j2-targ_y)**2 < self.r**2:
                    out[i2, j2] = 1
        return out

    def make_batch(self, n):
        for _ in range(n):
            self.ones_batch.append(self.one_patch())

    def simulate(self, pixel_value, fac=12):
        '''pixel value in [0,1]'''
        n_circles = -fac*np.log(1.001-pixel_value)  # float
        # ceil = np.floor(n_circles)
        # if rd.random()<n_circles-ceil:
        n_circles = int(np.random.randn()*2+n_circles)
        print(n_circles)
        # else:
        #   n_circles = int(n_circles)+1
        p = np.zeros((self.size, self.size))
        m = len(self.ones_batch)
        for _ in range(n_circles):
            p += self.ones_batch[rd.randint(0, m-1)]
        return np.minimum(p, 1)


def check_uniformity(size=11):
    P = NoisePatchGenerator(size)

    # check uniformity
    P.make_batch(10000)
    p = np.zeros((size, size))
    for e in P.ones_batch:
        p += e
    print(np.min(p), np.max(p))


def check_value(size=11):
    '''returns '''
    arr = []
    N = 100
    P = NoisePatchGenerator(size)
    P.make_batch(10000)

    for i in range(1, N+1):
        s = 0
        for _ in range(200):
            patch = P.simulate(i/N, 13.5)
            s += np.sum(patch)
        arr.append(s/200/size**2)
    arr = np.array(arr)
    print(np.sqrt(np.max((arr-np.linspace(0, 1, N))**2)))
