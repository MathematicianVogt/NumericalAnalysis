#Runge Kutta Fourth Order Numerical
#Ryan Vogt Applied Mathematics and Computer Science Major at RIT
import pylab
import math
class RungeKutta:
	 def __init__(self,differentialEquation,a,b,n,IC):
	 	self.differentialEquation=differentialEquation
	 	self.a=float(a)
	 	self.b=float(b)
	 	self.IC=float(IC)
	 	self.n=n


	 def evalFun(self,differentialEquation,ti,yi):
	 	y=yi
	 	t=ti
	 	return eval(differentialEquation)
	 def rungeKutta(self):
	 	h=(self.b-self.a)/self.n
	 	inputs=[]
	 	outputs=[]
	 	t=float(self.a)
	 	w=float(self.IC)
	 	inputs.append(t)
	 	outputs.append(w)
	 	for i in range(1,self.n+1):
	 		k1=self.evalFun(self.differentialEquation,t,w)
	 		k2=self.evalFun(self.differentialEquation,t +(h/2.0),w+(float(h*k1)/2.0))
	 		k3=self.evalFun(self.differentialEquation,t +(h/2.0),w+(float(h*k2)/2.0))
	 		k4=self.evalFun(self.differentialEquation,t +(h),w+(float(h*k3)))
	 		w=w+((h/6.0)*(k1+(2*k2)+(2*k3)+k4))
	 		t=self.a+(i*h)
	 		inputs.append(t)
	 		outputs.append(w)

	 	return inputs,outputs


	 def generateSolution(self):
	 	inputs,outputs=self.rungeKutta()
	 	print self.showOutput(inputs,outputs)
	 	pylab.title("Solution to y'=" +self.differentialEquation)
	 	pylab.plot(inputs,outputs,'r.')
	 	xlow=min(inputs)
	 	xhigh=max(inputs)
	 	ylow=min(outputs)
	 	yhigh=max(outputs)
	 	pylab.ylim([math.ceil(ylow-0.5*(yhigh-ylow)), math.ceil(yhigh+0.5*(yhigh-ylow))])
	 	pylab.xlim([math.ceil(xlow-0.5*(xhigh-xlow)), math.ceil(xhigh+0.5*(xhigh-xlow))])
	 	pylab.show()
	 	print "Done"
	 

	 def showOutput(self,input,output):
	 	solutionOutput="t------y(t)" +"\n"
	 	for x in range(len(input)):
	 		part = str(input[x]) + "------" + str(output[x]) +"\n"
	 		solutionOutput=solutionOutput+part

	 	return solutionOutput





x=RungeKutta("math.cos(t)",0,10,10000,0)
x.generateSolution()




