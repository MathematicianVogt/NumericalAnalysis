import math
from numericDifferentiation import numericDer
class NewtonsMethod:
	def __init__(self,function,p0,N,tol):
		self.function=function
		self.p0=float(p0)
		self.N=N
		self.tol=tol
		self.x=numericDer(self.function,self.p0,.00001)
	def evalFun(self,function,p):
		x=p
		return eval(function)
	def getRoot(self):
		
		i=1
		while(i<self.N):
			p=self.p0 - (self.evalFun(self.function,self.p0)/self.x.getDerivative())

			if((math.fabs(self.p0-p))<=self.tol):
				return p
				break
			i=i+1
			self.p0=p
			self.x.updateEvaluationPoint(self.p0)


t=NewtonsMethod("math.pow(x,2)-(4*x)+4",1000,1000,0)
print "Solution Found at " + str(t.getRoot())
