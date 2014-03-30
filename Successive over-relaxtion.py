from scipy import *
from numpy import *

class SOR:
	def __init__(self,A,b,TOL,x,w):
	 	self.a=mat(A)
	 	self.b=mat(b).T
	 	self.x=mat(x).T
	 	self.tol=TOL
	 	self.w=w
	def SORAlgo(self):
	 	A=self.a
	 	print "condition number of A " + str(linalg.cond(A)) +"\n"
	 	b=self.b
	 	x=self.x
	 	w=self.w
	 	D=diag(diag(A))
	 	L=tril(A)-D
	 	U=A-L-D
	 	xn1=((D+(w*L)).I)*(w*b - (w*U +(w-1)*D)*x)
	 	while(math.fabs(np.linalg.norm((x-xn1),2))>TOL):
	 		x=xn1
	 		xn1=((D+(w*L)).I)*(w*b - (w*U +(w-1)*D)*x)

	 	print "Soltuion found within " + str(self.tol)+ "\n" + str(xn1)

x=SOR('[2 2; 4 7]','[8,20]', .1, '[1,1]',1.1)
x.SORAlgo()
