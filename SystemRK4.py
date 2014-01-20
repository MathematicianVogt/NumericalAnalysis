#Written by Ryan Vogt @ RIT
#Approximate to solution to N differentiation equations with initial conditions

#from RKFour import RungeKutta
import math
import pylab

class SystemSolver:
	def __init__(self,listOfEquations,listofIC,a,b,N):
		self.listOfEquations=listOfEquations
		self.listofIC=listofIC
		self.a=a
		self.b=b
		self.N=N
	def evalFunc(self):
		pass
	def generateSolution(self):
		pass

	def makeODELIST(self,listOFODE):
		return listOFODE.split(",")
	def makeICLIST(self,listOFIC):
		return listOFIC.split(",")
	def SystemAlgo(self):
		myODES=self.makeODELIST(self.listOfEquations)
		myICS=self.makeICLIST(self.listofIC)
		numOfODE=len(myODES)
		h=(self.b-self.a)/float(self.N)
		t=self.a
		solutions=self.setBasicIC(myICS,numOfODE)
		
	def setBasicIC(self,myICS,numOfODE):
		solutionForODE=[]
		for i in range(0,numOfODE):
			currentList=[float(myICS[i])]
			solutionForODE.append(currentList)
		return solutionForODE

System=SystemSolver("y,t,y,y","0,1,2,3",1,2,1000);
System.SystemAlgo()