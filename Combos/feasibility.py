'''
Created on 2 Dec 2015

@author: s1144899
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
r = 0
for u in getOrderedColDec(6,32,False):
    r+=1
    #print u
print r