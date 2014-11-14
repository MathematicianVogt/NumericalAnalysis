import math


k=.01
h=.1


x=np.arange(0,300,k)
y=np.arange(0,100,h)
lastSol[]
currentSol=[]
fullSolutionList=[]

def addTuples(a,y,x,z):
	a.append((y,x,z))
def createNewSolution(a,y,x,z):
	a.append((y,x,z))

for t in y:
	lastSol.append(0)
	


for xo in range(0,len(x)):
	for yo in range(0,len(y)):
		if((yo==0 or yo==len(y)-1) and xo==0):
			

		elif(yo==0 or yo==len(y)-1):
			createNewSolution(fullSolutionList,y[yo],x[xo],0)
		else


