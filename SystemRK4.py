#Written by Ryan Vogt @ RIT
#Approximate to solution to N differentiation equations with initial conditions
#define variables as indepedent variable then all other variables y1....yn
import math
import pylab

class SystemSolver:
	def __init__(self,odeVars,ODES,ICS,a,b,N):
		self.vars=odeVars
		self.ODES=ODES
		self.ICS=ICS
		self.a=a
		self.b=b
		self.N=N
	
	def lengthOfList(self,myList):
		return len(myList)
	def parseStringintoList(self,string):
		return string.split(',')
	def lastElementofList(self,myList):
		basicList=[myList[-1]]
		return basicList
	
	def generateLastElementsOfSolution(self,myList):

		if(len(myList)==1):
			return float(myList[0][-1])

		return float(myList[0][-1]),self.generateLastElementsOfSolution(myList[1:])
	def combineListsToTuple(self,tlist,myTuple):
		thisList=list(myTuple)
		return tuple(tlist+thisList)

	def ajustTuple(self,tPlus,wPlus,wMultuplier,theTuple):
		myTuple=list(theTuple)
		myTuple[0]=myTuple[0]+tPlus
		for x in range(1,len(list(myTuple))):
			myTuple[x]=myTuple[x] +(wMultuplier)*wPlus
		return tuple(myTuple)

	
	def SolveSystemAndGraphSolution(self):
		h=(self.b-self.a)/float(self.N)
		lambdaODES=[]
		
		independentVariableslist=[]
		varsForOdes=self.vars
		ICS=self.parseStringintoList(self.ICS)
		ODES=self.parseStringintoList(self.ODES)
		solutionList=[[] for x in range(self.lengthOfList(ICS))]
		#establish indepdent variable list
		independentVariableslist.append(self.a)
		#establish IC
		for x in range(self.lengthOfList(ICS)):
			solutionList[x].append(ICS[x])

		#form ODES
		for x in ODES:
			lambdaString="lambda " + varsForOdes + ":" + x
			lambdaODES.append(eval(lambdaString)) 
		
		for x in range(1,self.N+1):
			starting=0
			basicEvaluation=self.generateLastElementsOfSolution(solutionList)
			totalEvaluationTuple=self.combineListsToTuple(self.lastElementofList(independentVariableslist),basicEvaluation)
			for lambdaODE in lambdaODES:
				currentODE=lambdaODE
				k1=h*currentODE(*totalEvaluationTuple)
				k2=h*currentODE(*self.ajustTuple(h/2.0,k1,.5,totalEvaluationTuple))
				k3=h*currentODE(*self.ajustTuple(h/2.0,k2,.5,totalEvaluationTuple))
				k4=h*currentODE(*self.ajustTuple(0,k3,1,totalEvaluationTuple))
				w=float(solutionList[starting][-1])+(k1+(2*k2)+(2*k3)+k4)/6.0
				print str(w)
				solutionList[starting].append(w)
				starting=starting+1

				#adding more later
			newT=self.a+(x*h)
			independentVariableslist.append(newT)

		for x in solutionList:
			pylab.plot(independentVariableslist,x)
		pylab.show()


x=SystemSolver("t,x,y","y,-x","0,1",0,6.28,1000)
x.SolveSystemAndGraphSolution()





