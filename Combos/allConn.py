'''
Created on 30 Nov 2015

@author: s1144899
'''
import numpy as np
import copy
def getAllMat(noNodes,w):
    # start with highest:
    newCol = (w-1)*np.ones(noNodes*noNodes,'int')
    # go through them and convert them
    c = noNodes*noNodes-1
    while True:
        if newCol[c] != 0:
            isOK = True
            newMat = np.reshape(copy.deepcopy(newCol),(noNodes,noNodes))
            # set the middles equal to zero:
            for x in range(noNodes):
                newMat[x,x]=0
            for x in range(noNodes):
                if np.sum(newMat[x,:])==0:
                    isOK = False
                    break
                if np.sum(newMat[:,x])==0:
                    isOK = False
                    break
            if isOK == True:
                yield newMat
            newCol[c] -= 1
            newCol[c+1:] = w-1
            c = noNodes*noNodes-1
        else:
            if c!=0:
                c-=1
            else:
                return

g = getAllMat(4,2)
r = 0
for f in g:
    #print f
    r += 1
print r