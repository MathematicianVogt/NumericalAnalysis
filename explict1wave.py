
from numpy import *
import scipy
import numpy as np
import math
import scipy.sparse as l
from plot import Graph3DSolution
import numpy.linalg as lin
import math

#explict case w(x)=2
#
#
#
#


def addTuples(a,y,x,z):
	a.append((y,x,z))
def createNewLineSolution(a,x,yList,solList):
	
	for t in range(0,len(yList)):
		addTuples(a,yList[t],x,solList.item(t))
		print solList.item(t)
	
		


def firstExplict():
	currentSol=[]
	lastSol=[]
	nextSol=[]
	tmax=300
	k=.1
	h=1


	x=np.arange(0,300,k)
	y=np.arange(0,100,h)
	currentSol=mat(np.zeros(len(y))).T

	initCon=[]
	for g in range(0,len(y)):
		initCon.append(((math.pi)/100.0)*math.sin(((math.pi)/100.0)*y[g]))


	Nx=len(y)
	r=(k**2)/(h**2)
	iden=linspace(1,1,Nx)
	d_main = 2*(1-r)*iden  # values that will go on main diagonal
	d_sub = r*iden     # values that will go on subdiagonal
	d_super = r*iden     # values that will go on superdiagonal
	data = [d_sub, d_main, d_super]   # list of all the data
	diags = [-1,0,1]                  # which diagonal each vector goes into
	A = l.spdiags(data,diags,Nx,Nx,format='csc')  # create the matrix
	A[0,0]=0
	A[Nx-1,Nx-1]=0
	A[Nx-1,Nx-2]=0





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
		#first time step using boundary condition
		if(currentStep==0):
			lastSol=currentSol
			currentSol=np.linalg.inv(I.todense()-C.todense())*(A*currentSol -2.0*h*C.todense()*mat(initCon).T)
			createNewLineSolution(wholeSolution,currentStep,y,currentSol)
		#general case of updating after first step
		else:
			newSol=A*currentSol+C*lastSol
			lastSol=currentSol
			currentSol=newSol
			createNewLineSolution(wholeSolution,currentStep,y,newSol)
		currentStep=currentStep+k



	Graph3DSolution(wholeSolution,"Wave Equation" ,"y","x","f")

def firstImplict():
	currentSol=[]
	lastSol=[]
	nextSol=[]
	tmax=300
	k=.1
	h=.5


	x=np.arange(0,300,k)
	y=np.arange(0,100,h)
	currentSol=mat(np.zeros(len(y))).T

	initCon=[]
	for g in range(0,len(y)):
		initCon.append(((math.pi)/100.0)*math.sin(((math.pi)/100.0)*y[g]))


	Nx=len(y)
	r=(k**2)/(h**2)
	iden=linspace(1,1,Nx)
	d_main = (1+2*r)*iden  # values that will go on main diagonal
	d_sub = -r*iden     # values that will go on subdiagonal
	d_super = -r*iden     # values that will go on superdiagonal
	data = [d_sub, d_main, d_super]   # list of all the data
	diags = [-1,0,1]                  # which diagonal each vector goes into
	A = l.spdiags(data,diags,Nx,Nx,format='csc')  # create the matrix
	'''
	A[0,0]=0
	A[Nx-1,Nx-1]=0
	A[Nx-1,Nx-2]=0
	'''




	iden=linspace(1,1,Nx)
	d_main = 2*iden  # values that will go on main diagonal
	d_sub = 0*iden     # values that will go on subdiagonal
	d_super = 0*iden     # values that will go on superdiagonal
	data = [d_sub, d_main, d_super]   # list of all the data
	diags = [-1,0,1]                  # which diagonal each vector goes into
	B= l.spdiags(data,diags,Nx,Nx,format='csc')  # create the matrix
	B[Nx-1,Nx-1]=0
	B[0,0]=0


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


	denseA=A.todense()
	denseB=B.todense()
	denseC=C.todense()

	while(currentStep<=tmax):
		#first time step using boundary condition
		if(currentStep==0):
			lastSol=currentSol
			currentSol=np.linalg.inv(denseA-denseC)*(denseB*currentSol -2.0*h*denseC*mat(initCon).T)
			createNewLineSolution(wholeSolution,currentStep,y,currentSol)
		#general case of updating after first step
		else:
			newSol=np.linalg.inv(denseA)*(denseB*currentSol +denseC*lastSol)
			lastSol=currentSol
			currentSol=newSol
			createNewLineSolution(wholeSolution,currentStep,y,newSol)
		currentStep=currentStep+k



	Graph3DSolution(wholeSolution,"Wave Equation" ,"y","x","f")

firstImplict()