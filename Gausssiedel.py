#Author Ryan Vogt

from scipy import *
from numpy import *
import numpy as np
import math

class gausssiedel:
	def __init__(self,A,b,TOL,x):
	 	self.a=mat(A)
	 	self.b=mat(b).T
	 	self.x=mat(x).T
	 	self.tol=TOL
	def gaussAlgo(self):
	 	A=self.a
	 	print "condition number of A " + str(linalg.cond(A)) +"\n"
	 	b=self.b
	 	x=self.x
	 	L=tril(A)
	 	U=A-L
	 	TOL=self.tol
	 	counter=0
	 	print L
	 	print U
	 	xn1=(L.I*(b-U*x))

	 	while(math.fabs(np.linalg.norm((x-xn1),2))>TOL):
	 		x=xn1
	 		xn1=(L.I*(b-U*x))
	 		counter++

	 	print "Soltuion found within " + str(self.tol)+ "\n" + str(xn1) + " in " +str(counter) "itterations"

x=gausssiedel('[2 2; 4 7]','[8,22]', .001, '[1,1]')
x.gaussAlgo()
