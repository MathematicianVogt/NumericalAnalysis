from scipy import *
from numpy import *
import numpy as np
import math

class Power:
	def __init__(self,A,b):
	 	self.a=np.matrix(A)
	 	self.b=np.matrix(b).T
	 	
	def Algo(self):
	 	
	 	A=self.a
	 	b=self.b
	 


	 	for x in range(0,100):
			nonnorm=(A*b)
			b=(A*b)/np.linalg.norm(A*b,2)

		print str(nonnorm)

x=Power('[10 -12 -6; 5 -5 -4; -1 0 3]','[4,2,3]')
x.Algo()