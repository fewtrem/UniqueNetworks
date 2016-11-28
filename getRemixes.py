'''
Created on 24 Nov 2015

@author: s1144899

the input is ordered!

'''
import numpy as np
import copy
# get the allowed remixes (reorgerings by size):
# (alg: without replacement get all orders (descending) from the newM input (i.e. what we just excluded from the above list))
# we can generate these and store in an array as we will need them more than once...
'''
take in an ordered mix:
e.g.[a][a][b][c]
we need to get all unique mixes out IN ORDER (ascending):
[a][a][c][b]
[a][b][a][c]
[a][c][a][b]
[b][a][a][c]... etc.
'''
def getRemixes(orig,w):
    #calculate pool of numbers:
    tabulate = np.zeros(w+1,'int')
    outgoing = copy.deepcopy(orig)[::-1]
    d = len(orig)-1
    goRet = [copy.deepcopy(outgoing)]
    while True:
        #see if there are any lower values:
        if sum(tabulate[outgoing[d]+1:]) !=0:
            # update the tabulation:
            tabulate[outgoing[d]]+=1
            # refill as max ordered:
            # get nonzero values:
            boolC = tabulate[outgoing[d]+1:]!=0
            # find the lowest value that we can allocate:
            ed = int(outgoing[d]+np.argmax(boolC)+1)
            # allocate it:
            tabulate[ed] -= 1
            outgoing[d] = ed
            # now move to the next one up to allocate it:
            d+=1
            t=0
            # now fill back up:
            while d < len(outgoing):
                while t < w:
                    if tabulate[t] != 0:
                        # allocate it:
                        outgoing[d] = t
                        tabulate[t] -= 1
                        d+=1
                    else:
                        t+=1
            goRet.append(copy.deepcopy(outgoing))
            
            d = len(orig)-1
        else:
            tabulate[outgoing[d]]+=1
            d -= 1
            if d == -1:
                return goRet
'''
for t in getRemixes([2,1,1],3):
    print t
'''



# Also a function to generate the slots we have for arranging the ordered ambiguous new nodes in:
'''
Need to be equal or increasing in slot size:
e.g. 7 new nodes:
[A][A][A][B][B][B][B] OK
[A][A][B][B][C][C][C] OK
[A][B][C][C][D][D][E] NOT OK
'''
# return [division list]
# [division list] as [0,0,1,1,2,2,2] etc.
def getSlotCombos(noNew):
    if noNew == 1:
        yield [1]
        return
    # store how many nodes are assigned to each number:
    numberOfNodes = np.zeros(noNew,'int')
    numberOfNodes[0] = noNew
    '''
    now we want to get an ordered version of this such that they all add up to the same number,
    e.g.
    4000
    3100
    2200
    2110
    ...
    '''
    # go through them and convert them
    c = noNew-2
    while True:
        #if numberOfNodes[c] > 1:
        if numberOfNodes[c] > 1:
            if numberOfNodes[c]-numberOfNodes[c+1]>1:
                yield numberOfNodes
                numberOfNodes[c] -= 1
                numberOfNodes[c+1] += 1
                c = noNew-2
            elif numberOfNodes[c]-numberOfNodes[c+1]==1:
                d = c+2
                cnue = True
                while d < noNew  and cnue == True:
                    if numberOfNodes[c+1]!=numberOfNodes[d]:
                        yield numberOfNodes
                        numberOfNodes[c] -= 1
                        numberOfNodes[d] += 1
                        c = noNew-2
                        cnue = False
                    d+=1
        else:
            if c!=0:
                c-=1
            else:
                yield numberOfNodes
                return
'''
for t in getSlotCombos(3):
    print t
'''


# generate a list of potential combos for this number of nodes:
# (alg: get all ORDERED combinations from theRemixes without replacement)
# a generator:
# simply returns numbers in the inputRemixes array!
def getAllotments(noDivisions,noRemixes):
    # input remixes are unique, and returned in ascending order so we simply need to go through and assign them:
    # start with the heaviest (should not matter which)
    newOrder = np.zeros(noDivisions,'int')
    for i in range(noDivisions):
        newOrder[i] = noRemixes-noDivisions+i
    # now let's go through and lower each one:
    c = 0
    while True:
        # lowest is now c (this min)
        if newOrder[c] != c:
            yield newOrder
            #reduce value:
            newOrder[c] -=1
            newOrder[:c] = range(newOrder[c]-c,newOrder[c])
            # reset c:
            c = 0
        else:
            # Note -2 not -1 as last column must be kept the same!
            if c>noDivisions-2:
                yield newOrder
                return
            else:
                c+=1

            
'''
import datetime
a = datetime.datetime.now()
t = getRemixes([3,2],4)
b = datetime.datetime.now()
print b-a, "seconds"
y = getAllotments(1,len(t))
for x in y:
    print x
print len(t)
'''