#Author Ryan Vogt

from scipy import *
from numpy import *

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
	 	xn1=(D.I*(b-R*x))

	 	for x in range(0,10000):
	 		x=xn1
	 		xn1=(D.I*(b-R*x))

	 	print "Soltuion found within " + str(self.tol)+ "\n" + str(xn1)

x=jacobi('[5 25; 1 3]','[10,18]', .1, '[1,1]')
x.jacobiAlgo()
