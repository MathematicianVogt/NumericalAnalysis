from scipy import *
from numpy import *
import numpy.linalg
a=mat('[1 2 ; 3 4]')
b=2*a
#print tril(a)
#print triu(a)
c=mat('(1,1)').T;
d=mat('(1,1)').T
e=mat('[1,3]').T


print vdot(c,d)