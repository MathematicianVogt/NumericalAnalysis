import math
class numericDerivative:
	def __init__(self,function,a,h):
		self.function=function
		self.a=float(a)
		self.h=float(h)
	def evalfunction(self,function,p):
		x=p
		return eval(function)

	def getDerivative(self):
		return ((self.evalfunction(self.function,self.a+self.h)-self.evalfunction(self.function,self.a))/self.h)

x=numericDerivative("math.pow(x,2)",5.0,.0001)
print(str(x.getDerivative()))