'''
Created on 25 Nov 2015

@author: s1144899
'''
import copy
'''
AmbigStore has simple structure:
[[[0],[1,2],[1,2],[3],[4,5,6],[4,5,6],[4,5,6]]]

we score each position using number of ambigs (max n)
'''
import numpy as np
def updateAmbigStore(ambigStore,newMat,nodesDone,rowsDone,numDoing):
    stopThis = False
    while stopThis == False:
        # let's make a copy of the new Matrix too as we are going to edit that:
        scorer = copy.deepcopy(newMat[0:nodesDone+numDoing,0:nodesDone+numDoing])
        scorer[rowsDone,nodesDone:] = 0
        # create a mapping:
        mapping = {}
        mapVal = 1
        NOi = 0
        while NOi < len(ambigStore[0]):
            thisAmb = ambigStore[0][NOi]
            for i in thisAmb:
                mapping[i] = mapVal
            NOi += len(thisAmb)
            mapVal += 1
        for i in range(nodesDone,nodesDone+numDoing):
            mapping[i] = mapVal
        scoreMulti = mapVal*mapVal
        # mapVal is the highest value...
        # now let's look at the incoming nodes and label them (that is the columns)
        for x in range(scorer.shape[0]):
            for y in range(scorer.shape[0]):
                scorer[x,y] = mapVal*mapping[x]+mapping[y]+(scorer[x,y]*scoreMulti)
        # ambiguous nodes have the same incoming AND outgoing, so will have a unique sum for the cols and rows:
        ambigStoreNew = []
        ambigLoc = [0]
        ambigLast = [np.sum(scorer[:,0]),np.sum(scorer[0,:])]
        for n in range(1,nodesDone):
            thisAmbigScore = [np.sum(scorer[:,n]),np.sum(scorer[n,:])]
            if ambigLast[0]==thisAmbigScore[0] and ambigLast[1]==thisAmbigScore[1]:
                ambigLoc.append(n)
            else:
                for i in range(len(ambigLoc)):
                    ambigStoreNew.append(ambigLoc)
                ambigLoc = [n]
                ambigLast = thisAmbigScore
        for i in range(len(ambigLoc)):
            ambigStoreNew.append(ambigLoc)
        ambigStoreNew = ambigStoreNew
        # see if we have updated the ambigScore?
        if np.array_equal(ambigStoreNew,ambigStore[0]):
            stopThis = True
        ambigStore[0] = ambigStoreNew
    return ambigStore
    