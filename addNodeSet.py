'''
Created on 24 Nov 2015

@author: s1144899

in:
noUN - number of unique nodes so far, (to be returned..)
newMatrix - the new matrix so far
nodesD - number of nodes already done...
func - function to run on the matrix as func(M)
retStore - reference to place to store results of the function
weightsSum - pre calculated weights sum
w - num of weights
ambigStore - storage of ambiguities:
[0] - summary about what is possible for each node: [[1],[3,2],[3,2],[4]] etc.

returns...
'''
import numpy as np
import copy
from getOrderedCol import getOrderedMix
from getRemixes import getRemixes,getSlotCombos,getAllotments
from updateAmbigStore import updateAmbigStore
# add the columns with zero in anything bigger:
def addColSet(noUN,newMatrix,nodesD,func,retStore,weightsSum,w,ambigStore):
    prevColDep = False
    for newj in range(1,newMatrix.shape[0]-nodesD+1):
        maxnodesD = nodesD+newj
        addCol(noUN,newMatrix,nodesD,nodesD,func,retStore,weightsSum,w,ambigStore,prevColDep,maxnodesD)
# add identical columns:
def addCol(noUN,newMatrix,nodesD,rowsToFill,func,retStore,weightsSum,w,ambigStore,prevColDep,maxnodesD):
    # number of columns we could add at this level is number of nodes left:
    # OK to do loop as remaining ones will do rest of matrix
    for newi in range(1,maxnodesD-nodesD+1):
        NOi = 0
    # going to do this recursively to ensure that the ambigStore is correct!
        populateColPart(noUN,newMatrix,nodesD,rowsToFill,func,retStore,weightsSum,w,ambigStore,NOi,newi,prevColDep,maxnodesD)


#NOTE: It MUST not have all non-zeros in the final ambig as new column could not be in previous set!

# prevColDep - must be lower than previous column until we differ from it!
def populateColPart(noUN,newMatrix,nodesD,rowsToFill,func,retStore,weightsSum,w,ambigStore,NOi,noNew,prevColDep,maxnodesD):
    # Copy the ambiguous store so that we modify it here:
    # Label for this ambigStore
    thisPos = ambigStore[0][NOi]
    # now get the number of values we can add:
    lastOne = NOi+len(thisPos)==rowsToFill
    yieldFirst = True
    if prevColDep == True:
        maxOLD = newMatrix[NOi:(NOi+len(thisPos)),nodesD-1]
        if lastOne == True:
            yieldFirst = False
    else:
        maxOLD = np.zeros(len(thisPos),'int')
    # boolA should only be 
    genAm = getOrderedMix(len(thisPos),w,lastOne,maxOLD,yieldFirst)
    for newM in genAm:
        # get the allowed remixes (reorgerings by size):
        # (alg: without replacement get all orders (descending) from the newM input (i.e. what we just excluded from the above list))
        # we can generate these and store in an array as we will need them more than once...
        theRemixes = getRemixes(newM,w)
        # decide on how we are going to separate up the new remixes:
        # note that the first one MUST be the maximum we have chosen, the rest can be ordered (descending) versions
        # we also want the number of repeated ones to increase...
        
        # get a list of the slots we can put them in:
        # A GENERATOR:
        slotCombos = getSlotCombos(noNew)
        # go through the list of slot combos and fill them up
        # the number that are nonzero in the return matrix from slotComb:
        numberNonZero = 1
        theAllotments = getAllotments(1,len(theRemixes))  
        for slotComb in slotCombos:
            # update the number we have:
            if numberNonZero<len(slotComb):
                if slotComb[numberNonZero] != 0:
                    numberNonZero+=1
                    if numberNonZero <= len(theRemixes):
                        # NOT a generator:
                        theAllotments = getAllotments(numberNonZero,len(theRemixes)) 
            # check we don't have more to allot than we have remixes!  
            if numberNonZero <= len(theRemixes):    
                # generate a list of potential combos for this number of nodes:
                # (alg: get all ordered combinations from theRemixes without replacement)
                # us the generator function for this as we haven't stored it:
                for thisAllotment in theAllotments:
                    # the thisAllotment just retruns the order we should assign the remixes to the allotment:
                    # fill the slotComb with a range of theRemixes:
                    #newMatrix[NOi:(NOi+len(thisPos)),nodesD:(nodesD+noNew)] = np.tile(np.matrix(newM).transpose(),(1,noNew))
                    j = 0
                    k = 0
                    while j < noNew:
                        #print "Adding ",theRemixes[thisAllotment[k]],"to",range(NOi,(NOi+len(thisPos))),range(nodesD+j,int(nodesD+j+slotComb[j]))
                        for l in range(slotComb[j]):
                            newMatrix[NOi:(NOi+len(thisPos)),nodesD+j+l:nodesD+j+l+int(slotComb[j])] = np.asmatrix(theRemixes[thisAllotment[k]]).transpose()
                        j += slotComb[j]
                        k+= 1
                    # DO STUFF, check for ambiguities etc.
                    # ONLY CHECK ONES THAT WE HAVE SET!  AS MATRIX MAY HAVE OTHER VALUES ELSEWHERE THAT HAVE NOT BEEN UPDATED YET! 
                    ambigStore = updateAmbigStore(ambigStore,newMatrix,nodesD,NOi+len(thisPos),noNew)
                    
                    if prevColDep == True:
                        if newM != maxOLD:
                            prevColDep = False
                # If we are still less than the required length of this column, then look at the next ambiguity
                    NOj = NOi+len(thisPos)
                    if NOj < rowsToFill:
                        # Check prevColDep
                        populateColPart(noUN,newMatrix,nodesD,rowsToFill,func,retStore,weightsSum,w,ambigStore,NOj,noNew,prevColDep,maxnodesD)
                    else:
                        newMatrix[NOj:,nodesD:nodesD+noNew] = 0
                        newNodesD = nodesD+noNew
                        #print ambigStore
                        for i in range(noNew):
                            ambigStore[0].append(range(nodesD,newNodesD))
                        #print noNew,">",ambigStore
                        if newNodesD<newMatrix.shape[0]:
                            if newNodesD==maxnodesD:
                                addColSet(noUN,newMatrix,newNodesD,func,retStore,weightsSum,w,ambigStore)
                            else:
                                addCol(noUN,newMatrix,newNodesD,rowsToFill,func,retStore,weightsSum,w,ambigStore,True,maxnodesD)
                        else:
                            # Check that there are no empty rows... (i.e. that they all go from to places!)
                            OKM = True
                            for i in range(0,newMatrix.shape[0]-1):
                                if sum(newMatrix[i,:])==0:
                                    OKM = False
                            if OKM == True:
                                # we now have a matrix!!
                                #print "A matrix has been born:"
                                
                                #print newMatrix,ambigStore[0]
                                noUN[0]+=1
            else:
                break

