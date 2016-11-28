'''
Created on 24 Nov 2015

@author: s1144899

We will attempt to produce all the unique networks:


How will we know that they are unique, we would have to use a reordering algorithm??

'''

from datetime import datetime
from generateUniqueMatrices import generateUniqueMatrices

a = datetime.now()
gen = generateUniqueMatrices(7,2,None)
b = datetime.now()
c = float((b-a).seconds)/gen[0][0]
print b-a,"seconds"
print gen[0]
print c," per matrix"
