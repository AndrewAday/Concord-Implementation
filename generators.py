import numpy as np
import math

def test0():
    X = [0] * 100 + [1] * 100
    return X

def test1():
    X = np.zeros(1024)
    e = np.random.normal(size=1024)
    for t in np.arange(1, 484):
        X[t] = .75 * X[t-1] + e[t]
    for t in np.arange(484, 803):
        X[t] = 1.7 * X[t-1] - .75 * X[t-2] + e[t]
    for t in np.arange(803, 1024):
        X[t] = 1.25 * X[t-1] - .7 * X[t-2] + e[t]
    return X

def hazard(p):
    def geometric(t):
        return p * (1 - p) ** t
    return geometric

p = .4