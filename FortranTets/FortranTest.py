'''
Created on 5 Dec 2015

@author: s1144899
'''
import numpy as np
from datetime import datetime
import add
c = np.ones(2000000,dtype='complex')
d = np.ones(2000000,dtype='complex')
a = datetime.now()
e = add.zadd(c, d)
b = datetime.now()
print b-a
a = datetime.now()
e = c+d
b = datetime.now()
print b-a
