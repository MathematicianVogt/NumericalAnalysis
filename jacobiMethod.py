#Author Ryan Vogt

from scipy import *
from numpy import *
import numpy as np
import math

class jacobi:
	def __init__(self,A,b,TOL,x):
	 	self.a=mat(A)
	 	self.b=mat(b).T
	 	self.x=mat(x).T
	 	self.tol=TOL
	def jacobiAlgo(self):
	 	A=self.a
	 	print "condition number of A " + str(linalg.cond(A)) +"\n"
	 	b=self.b
	 	x=self.x
	 	R=diag(diag(A))
	 	D=A-R
	 	counter=0
	 	xn1=(D.I*(b-R*x))

	 	while(math.fabs(np.linalg.norm((x-xn1),2))>TOL):
	 		x=xn1
	 		xn1=(D.I*(b-R*x))
	 		counter++

	 	print "Soltuion found within " + str(self.tol)+ "\n" + str(xn1) + " in " +str(counter) "itterations"

x=jacobi('[5 25; 1 3]','[10,18]', .1, '[1,1]')
x.jacobiAlgo()
