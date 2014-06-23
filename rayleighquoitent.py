from scipy import *
from numpy import *
import numpy as np
import math

class RayQuo:
	def __init__(self,A,b,u):
	 	self.a=np.matrix(A)
	 	self.b=np.matrix(b).T
	 	self.u=u
	def Algo(self):
	 	
	 	A=self.a
	 	b=self.b
	 	u=self.u


	 	for x in range(0,100):
			b=(np.linalg.inv(A-(np.identity(3)*u))*b)/np.linalg.norm(A-(np.identity(3)*u)*b,2)
			print str(b)
			u=((b.T)*A*b)/((b.T)*b)
			u=float(u.item(0))
			print str(u)

		print str(b)
		print str(u)

x=RayQuo('[10 -12 -6; 5 -5 -4; -1 0 3]','[4,2,3]',2)
x.Algo()
