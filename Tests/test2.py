'''
Created on 24 Nov 2015

@author: s1144899
'''
import numpy as np
h = [3,4]
h = np.matrix(h)
print np.tile(np.matrix(h).transpose(),(1,2))

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        
f = combinations('ABBD',2)
for s in f:
    print s