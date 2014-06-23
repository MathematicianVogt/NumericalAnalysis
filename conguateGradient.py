#Author Ryan Vogt
#requirement that A is positive definite and symmetric. 
from scipy import *
from numpy import *
import numpy as np
import math

class conGradient:
	def __init__(self,A,b,TOL,x):
	 	self.a=np.matrix(A)
	 	self.b=np.matrix(b).T
	 	self.x=np.matrix(x).T
	 	self.tol=TOL
	def Algo(self):
	 	
	 	A=self.a
	 	b=self.b
	 	x=self.x
	 	xo=x
	 	ro=b-A*xo
	 	po=ro
	 	


	 	while(math.fabs(np.linalg.norm(ro,2))>self.tol):
	 		#print str(math.fabs(np.linalg.norm(ro,2)))
	 		ak=((ro.transpose())*ro)/((po.transpose())*A*po)
	 		xn=xo+(float(ak.item(0))*po)
	 		rn=ro-(float(ak.item(0))*A*po)
	 		temp=rn.transpose()
	 		bn=(temp*rn)/((ro.transpose())*ro)
	 		pn=rn+(float(bn.item(0))*po)
	 		xo=xn
	 		ro=rn
	 		po=pn
		print "Soltuion found within " + str(self.tol)+ "\n" + str(xn)

x=conGradient('[2 1 1; 1 2 1; 1 1 2]','[4,0,0]', .001, '[0,0,0]')
x.Algo()
