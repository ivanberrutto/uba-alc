import numpy as np

def norma(x,y):
    res = 0
    for i in x:
        res = res + (abs(i) ** y) 
    res = res ** (1/y)
    return res

assert(np.allclose(norma(np.array([1, 1]), 2), np.sqrt(2)))
assert(np.allclose(norma(np.array([1] * 10), 2), np.sqrt(10)))
assert(norma(np.random.rand(10), 2) <= np.sqrt(10))
assert(norma(np.random.rand(10), 2) >= 0)

def normaliza(lista,p):
    res = np.array
    i = 0
    for v in lista:
        res[i] = norma(lista[i],p)
        i = i+1
    return res


assert all(np.allclose(norma(x, 2), 1) for x in normaliza([np.array([1] * k) for k in range(1, 11)], 2))
assert all(not np.allclose(norma(x, 2), 1) for x in normaliza([np.array([1] * k) for k in range(1, 11)], 1))
assert all(np.allclose(norma(x, np.inf), 1) for x in normaliza([np.random.rand(k) for k in range(1, 11)], np.inf))
