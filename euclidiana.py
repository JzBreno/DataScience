import numpy as np
import random as rd


dados = [(rd.randrange(10), rd.randrange(10), rd.randrange(
    10), rd.randrange(10)) for i in range(2)]

a, b, c, d = dados[0]
e, f, g, h = dados[1]

dist = np.sqrt(np.square(a - e) + np.square(b - f) +
               np.square(c - g) + np.square(d - h))
print(dist)
