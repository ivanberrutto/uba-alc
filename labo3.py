import numpy as np

def norma(x,p):
    if(p=='inf'):
        mayor = 0
        for i in x:
            mayor = max(abs(i),mayor)
        return mayor
            
    res = 0
    for i in x:
        res = res + (abs(i) ** p) 
    res = res ** (1/p)
    return res

assert(np.allclose(norma(np.array([1, 1]), 2), np.sqrt(2)))
assert(np.allclose(norma(np.array([1] * 10), 2), np.sqrt(10)))
assert(norma(np.random.rand(10), 2) <= np.sqrt(10))
assert(norma(np.random.rand(10), 2) >= 0)

def normaliza(lista,p):
    res = []
    i = 0
    for v in lista:
        res.append( v / norma(v,p) )
    return res


assert (np.allclose(norma(x, 2), 1) for x in normaliza([np.array([1] * k) for k in range(1, 11)], 2))
assert ([not np.allclose( norma ( x , 2 ) , 1 ) for x in normaliza([ np.array([1]*k) for k in range(1, 11 ) ] , 1) ])
assert (np.allclose(norma(x, np.inf), 1) for x in normaliza([np.random.rand(k) for k in range(1, 11)], np.inf))


