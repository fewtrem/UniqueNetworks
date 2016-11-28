'''
Created on 24 Nov 2015

@author: s1144899

in:
n: number of neurons
w: number of weights for connections (including zero)

out: number of unique networks, will need to run functions inside this as too many produced, probably

'''

import numpy as np
from addNodeSet import addColSet
def generateUniqueMatrices(n,w,func):
    # counter for number of unique networks
    noUN = [0]
    # place to returnData:
    retStore = []
    # new matrix that will be used to execute later functions on:
    newMatrix = np.zeros((n,n),'int')
    weightsSum = -np.ones(n,'int')
    for i in range(n):
        weightsSum[i] = np.power(w,n-i)
    # Find the next node and run the function if we get to the end
    #(noUN,newMatrix,nodesD,func,retStore,weightsSum,w,ambigStore)
    #newMatrix = np.matrix("0 1 1 0 0 0;0 0 0 1 0 0;0 0 0 1 0 0;0 0 0 0 0 0;0 0 0 0 0 0;0 0 0 0 0 0")
    #ambigStore = [[[0],[1,2],[1,2],[3]]
    ambigStore = [[[0]]]
    nodesDone = 1
    addColSet(noUN,newMatrix,nodesDone,func,retStore,weightsSum,w,ambigStore)
    return noUN,retStore