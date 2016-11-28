'''
Created on 24 Nov 2015

@author: s1144899


This function is bascially equivalent to 
https://docs.python.org/2/library/itertools.html
combinations_with_replacement(iterable, r)

'''
import numpy as np
def getOrderedColDec(noNodes,w,boolA):
    # start with highest:
    newCol = (w-1)*np.ones(noNodes,'int')
    # go through them and convert them
    c = noNodes-1
    while True:
        if newCol[c] != 0:
            yield newCol
            newCol[c] -= 1
            newCol[c:] = newCol[c]
            c = noNodes-1
        else:
            if c!=0:
                c-=1
            else:
                if boolA == False:
                    yield newCol
                return
            
def getOrderedColAsc(noNodes,w,boolA):
    # start with lowest:
    newCol = np.zeros(noNodes,'int')
    # go through them and convert them
    c = noNodes-1
    while True:
        if newCol[c] != w-1:
            if newCol[noNodes-1] != 0 or boolA ==False:
                yield newCol
            newCol[c] += 1
            newCol[c:] = newCol[c]
            c = noNodes-1
        else:
            if c!=0:
                c-=1
            else:
                yield newCol
                return
            
def getOrderedMix(noNodes,w,boolA,miner,yieldFirst):
    # start with lowest:
    newCol = np.zeros(noNodes,'int')
    newCol[:] = miner[:]
    # go through them and convert them
    c = 0
    if yieldFirst == True:
        if newCol[noNodes-1] != 0 or boolA ==False:
            yield newCol
    while True:
        if newCol[c] != w-1:
            newCol[c] += 1
            newCol[:c] = newCol[c]
            if newCol[noNodes-1] != 0 or boolA ==False:
                yield newCol
            c = 0
        else:
            if c!=noNodes-1:
                c+=1
            else:
                return
'''
g = getOrderedMix(3,2,True,[1,1,1],False)
for h in g:
    print h
'''