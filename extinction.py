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

	def ajustTuple(self,tPlus,kMultiplier,theTuple,kjList):
		myTuple=list(theTuple)
		myTuple[0]=myTuple[0]+ tPlus
		for x in range(1,len(list(myTuple))):
			myTuple[x]=myTuple[x] +kMultiplier*kjList[x-1]
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
	#====================================
		for x in range(1,self.N+1):
			myEval=self.generateLastElementsOfSolution(solutionList)
			totalEvaluationTuple=self.combineListsToTuple(self.lastElementofList(independentVariableslist),myEval)
			k1j=[]
			k2j=[]
			k3j=[]
			k4j=[]
			for lambdaODE in lambdaODES:
				currentODE=lambdaODE
				k1j.append(h*currentODE(*totalEvaluationTuple))
			for lambdaODE in lambdaODES:
				currentODE=lambdaODE
				k2j.append(h*currentODE(*self.ajustTuple(h/2.0,.5,totalEvaluationTuple,k1j)))
			for lambdaODE in lambdaODES:
				currentODE=lambdaODE
				k3j.append(h*currentODE(*self.ajustTuple(h/2.0,.5,totalEvaluationTuple,k2j)))
			for lambdaODE in lambdaODES:
				currentODE=lambdaODE
				k4j.append(h*currentODE(*self.ajustTuple(h,1,totalEvaluationTuple,k3j)))
			starting=0
			for i in range(1,len(ODES)+1):
				wj=float(solutionList[starting][-1])+(k1j[i-1]+(2*k2j[i-1])+(2*k3j[i-1])+k4j[i-1])/6.0
				print str(wj)
				solutionList[starting].append(wj)
				starting=starting+1
			newT=self.a+(x*h)
			independentVariableslist.append(newT)

			
			
		
		#=================================================
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
		pylab.title("x(t) vs t")
		pylab.plot(independentVariableslist,solutionList[0])
		pylab.show()
		pylab.title("y(t) vs z(t)")
		pylab.plot(solutionList[1],solutionList[2])
		pylab.show()
		print "Done"



x=SystemSolver("t,x,y,z","-1*x*(1-x),2*y*(1-(y/((1-.5)*x +.5))) -.5*z, (1/18.7)*z*(1-(z/(1*y)))",".99,.75,.73",0,100,10000)
x.SolveSystemAndGraphSolution()

