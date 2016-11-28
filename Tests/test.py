'''
Created on 24 Nov 2015

@author: s1144899
'''
import itertools,sys
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    print tuple(pool[i] for i in indices)
    while True:
        # go through the number of outputs (backwards!)
        for i in reversed(range(r)):
            # break if we find the index is still not at the max, as we need to use it first!
            if indices[i] != n - 1:
                break
        # execute the else only if not broken out (we could mimic this with a check of our own)
        else:
            # so leave the function if and only if we didn't have to break...
            print "done"
            return
        # make the indices up to this point equal to 
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
        
g =  combinations_with_replacement(["A","V","C","D"],5)



print sys.getsizeof(g)
e = 0
for d in g:
    e+=1
print "x",e
    
for i in range(5):
    print i
    if i==2:
        break
else:
    print "D"
import numpy as np
print np.arange(5,-1,-1)