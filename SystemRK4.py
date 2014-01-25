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
		self.LegendForGraphs=[]
	
	def makeLegends(self):
		variableList=self.parseStringintoList(self.vars)
		ODEList=self.parseStringintoList(self.ODES)
		indepdentVariable=variableList[0]
		for x in range(len(ODEList)):
			self.LegendForGraphs.append("Solution curve for d" + str(variableList[x+1]) + "/d" + str(indepdentVariable) + " =" +str(ODEList[x]))


	def findLowest(self,myList):
		lowest=float(myList[0][0])
		for x in myList:
			for i in range(len(x)):
				if(float(x[i])<lowest):
					lowest=float(x[i])
		return lowest
	def findGreatest(self,myList):
		greatest=float(myList[0][0])
		for x in myList:
			for i in range(len(x)):
				if(float(x[i])>greatest):
					greatest=float(x[i])
		return greatest

	def lengthOfList(self,myList):
		return len(myList)
	def parseStringintoList(self,string):
		return string.split(',')
	def lastElementofList(self,myList):
		basicList=[myList[-1]]
		return basicList
	
	def generateLastElementsOfSolution(self,myList):
		finalList=[]
		for x in myList:
			finalList.append(float(x[-1]))
		return tuple(finalList)
	def combineListsToTuple(self,tlist,myTuple):
		thisList=list(myTuple)
		final=tlist+thisList
		return tuple(final)

	def ajustTuple(self,tPlus,wPlus,wMultuplier,theTuple):
		myTuple=list(theTuple)
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
			myEval=self.generateLastElementsOfSolution(solutionList)
			totalEvaluationTuple=self.combineListsToTuple(self.lastElementofList(independentVariableslist),myEval)
			for lambdaODE in lambdaODES:
				currentODE=lambdaODE
				k1=h*currentODE(*totalEvaluationTuple)
				k2=h*currentODE(*self.ajustTuple(h/2.0,k1,.5,totalEvaluationTuple))
				k3=h*currentODE(*self.ajustTuple(h/2.0,k2,.5,totalEvaluationTuple))
				k4=h*currentODE(*self.ajustTuple(0,k3,1,totalEvaluationTuple))
				w=float(solutionList[starting][-1])+(k1+(2*k2)+(2*k3)+k4)/6.0
				solutionList[starting].append(w)
				starting=starting+1

				#adding more later
			newT=self.a+(x*h)
			independentVariableslist.append(newT)
		

		self.makeLegends()
		legendNumber=0
		for x in solutionList:
			pylab.plot(independentVariableslist,x,label=self.LegendForGraphs[legendNumber])
			legendNumber=legendNumber+1
		legendNumber=0
		xlow=min(independentVariableslist)
		xhigh=max(independentVariableslist)
		ylow=self.findLowest(solutionList)
		yhigh=self.findGreatest(solutionList)
		
		pylab.ylim([math.ceil(ylow-0.5*(yhigh-ylow)), math.ceil(yhigh+0.5*(yhigh-ylow))])
	 	pylab.xlim([math.ceil(xlow-0.5*(xhigh-xlow)), math.ceil(xhigh+0.5*(xhigh-xlow))])
		pylab.legend()
		pylab.title("Solution to Systems of Ordinary Differential Equations")
		pylab.show()
		print "Done"


x=SystemSolver("t,x,y","y,-x","0,1",0,10,1000)
x.SolveSystemAndGraphSolution()





