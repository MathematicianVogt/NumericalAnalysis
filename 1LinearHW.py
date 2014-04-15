from scipy import *
from numpy import*
import scipy.linalg as s
import numpy.linalg as np
import math
b=mat('[2 4 6]').T
A=mat('[4 2 0; 4 4 2; 2 2 3]')
p,l,u=s.lu(A)
print p
print l
print u
#back subsitution chain to find solution
x=np.inv(u)*(np.inv(l)*(np.inv(p)*b))
print x


'''
OutPut:
A=PLU
[
[ 1.  0.  0.]
 [ 0.  1.  0.]       -------> P which is the idenity
 [ 0.  0.  1.]]

[[ 1.   0.   0. ]
 [ 1.   1.   0. ]    -------> L lower triangular matrix
 [ 0.5  0.5  1. ]]

[[ 4.  2.  0.]
 [ 0.  2.  2.]       ---------> U upper triangular matrix
 [ 0.  0.  2.]]

[[ 1.]
 [-1.]
 [ 2.]]				----------> x the solution to the system of Ax=U
 '''
