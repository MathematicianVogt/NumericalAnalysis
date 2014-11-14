
from numpy import *
import scipy
import numpy as np
import math
import scipy.sparse as l
from plot import Graph3DSolution
import numpy.linalg as lin
import math
def addTuples(a,y,x,z):
	a.append((y,x,z))
def createNewLineSolution(a,x,yList,solList):
	
	for t in range(0,len(yList)):
		addTuples(a,yList[t],x,solList.item(t))
		print solList.item(t)
	
		

def generateTimeMatrix(v0,t,lengthOfMatrix):
	row=1
	tau=1
	sigma=1
	g=980
	gamma=(row*tau*v0)/sigma
	w=gamma*math.sqrt(v0**2 +2*g*t)
	wprime=gamma/(math.sqrt(v0**2+2*g*t))
	Nx=lengthOfMatrix
	if(t==0):
		r=(k**2)/(h**2)
		rr=r=(k**2)/(2*h)
		iden=linspace(1,1,Nx)
		d_main = (1-(r*1.0/(w-1)))*iden  # values that will go on main diagonal
		d_sub = (1.0/(2.0*(w-1)))*(r+(rr*wprime))*iden     # values that will go on subdiagonal
		d_super = (1.0/(2.0*(w-1)))*(r-(rr*wprime))*iden      # values that will go on superdiagonal
		data = [d_sub, d_main, d_super]   # list of all the data
		diags = [-1,0,1]                  # which diagonal each vector goes into
		A = l.spdiags(data,diags,Nx,Nx,format='csc')  # create the matrix
		A[0,0]=0
		A[0,1]=0
		A[Nx-1,Nx-1]=0
		A[Nx-1,Nx-2]=0
	else:
		r=(k**2)/(h**2)
		rr=r=(k**2)/(2*h)
		iden=linspace(1,1,Nx)
		d_main = 2*(1-(r*(1.0/(w-1))))*iden  # values that will go on main diagonal
		d_sub = (1.0/((w-1)))*(r+(rr*wprime))*iden     # values that will go on subdiagonal
		d_super = (1.0/((w-1)))*(r-(rr*wprime))*iden      # values that will go on superdiagonal
		data = [d_sub, d_main, d_super]   # list of all the data
		diags = [-1,0,1]                  # which diagonal each vector goes into
		A = l.spdiags(data,diags,Nx,Nx,format='csc')  # create the matrix
		A[0,0]=0
		A[0,1]=0
		A[Nx-1,Nx-1]=0
		A[Nx-1,Nx-2]=0

	return A.todense()

def firstExplict(v0,initialData,thish,thisk):
	currentSol=[]
	lastSol=[]
	nextSol=[]
	tmax=300
	k=thisk
	h=thish


	x=np.arange(0,300,k)
	y=np.arange(0,100,h)
	currentSol=mat(np.zeros(len(y))).T




	Nx=len(y)
	iden=linspace(1,1,Nx)
	d_main = -1*iden  # values that will go on main diagonal
	d_sub = 0*iden     # values that will go on subdiagonal
	d_super = 0*iden     # values that will go on superdiagonal
	data = [d_sub, d_main, d_super]   # list of all the data
	diags = [-1,0,1]                  # which diagonal each vector goes into
	C = l.spdiags(data,diags,Nx,Nx,format='csc')  # create the matrix
	C[Nx-1,Nx-1]=0
	C[0,0]=0
	I=l.identity(Nx)
	currentStep=0
	wholeSolution=[]
	newSol=[]

	#print A.todense(


	while(currentStep<=tmax):
		currentMatrix=generateTimeMatrix(v0,currentStep,len(y))
		#first time step using boundary condition
		if(currentStep==0):
			lastSol=initialData
			currentSol=currentMatrix*initialData
			createNewLineSolution(wholeSolution,currentStep,y,currentSol)
		#general case of updating after first step
		else:
			newSol=currentMatrix*currentSol+C*lastSol
			lastSol=currentSol
			currentSol=newSol
			createNewLineSolution(wholeSolution,currentStep,y,newSol)
		currentStep=currentStep+k



	Graph3DSolution(wholeSolution,"Wave Equation" ,"y","x","f")
h=1.0
k=.1
space=np.arange(0,100,h)

IC1=[]
IC2=[]
IC3=[]



for x in space:
	IC1.append(math.sin((4.0*math.pi*x)/100.0))
IC1=mat(IC1).T

for p in space:
	IC2.append((p*(100.0-p)*(25.0-p))/math.pow(10.0,6))
IC2=mat(IC2).T
for u in space:
	IC3.append((u/100.0)*(1-(u/100.0))*math.exp(-(math.pow(u-25,2))/200.0))
IC3=mat(IC3).T


firstExplict(8.7,IC1,h,k)
firstExplict(8.7,IC2,h,k)
firstExplict(8.7,IC3,h,k)
firstExplict(20,IC1,h,k)
firstExplict(20,IC2,h,k)
firstExplict(20,IC3,h,k)
firstExplict(200,IC1,h,k)
firstExplict(200,IC2,h,k)
firstExplict(200,IC3,h,k)


