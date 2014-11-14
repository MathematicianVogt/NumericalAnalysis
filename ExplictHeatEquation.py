#EXPLICT HEAT EQUATION
from scipy import *
from numpy import *
import scipy as s
import numpy as np
import math
import scipy.sparse as l
from plot import Graph3DSolution
import numpy.linalg as lin

def addNewPoint(x,t,u):
	return (x,t,u)
def addTupleToList(a,List):
	List.append(a)
def showList(myList):
	print "Time-Concentration"
	for x in range(0,len(myList)):
		print str(myList[x][1]) + "      " + str(myList[x][2])

#variables
x0=0.0
x1=1.0
t0=0.0
t1=2.0
#use of stability condition D(dt/(dx)^2)<1/2
D=.4
V=2
Nx=4
h=.2865
k=.0441
r=(D*k)/h**2
iden=linspace(1,1,Nx)
d_main = (1-2*r)*iden  # values that will go on main diagonal
d_sub = r*iden     # values that will go on subdiagonal
d_super = r*iden     # values that will go on superdiagonal
data = [d_sub, d_main, d_super]   # list of all the data
diags = [-1,0,1]                  # which diagonal each vector goes into
A = l.spdiags(data,diags,Nx,Nx,format='csc')  # create the matrix

zeroVector=linspace(0,0,Nx)
realu0=matrix(zeroVector).T
zeroVector[0]=1
jumpu0=matrix(zeroVector).T

solutionList=[]

A[(A.shape[0]-1),-1]=(1-(2*r))
A[(A.shape[0]-1),-2]=2*r
A[0,0]=(1-2*r+((4*V*r)/(2*V+h)))
A[0,1]= (r+ r*((h-2*V)/(2*V+h)))
#print A.todense()


currentStep=0
newStep=jumpu0

while(currentStep<=t1):
	if(currentStep==0):
		newStep=A*newStep
		for a in range(0,len(realu0)):
			#print addNewPoint(a*h,currentStep,realu0.item(a))
			addTupleToList(addNewPoint(a*h,currentStep,realu0.item(a)),solutionList)
			currentStep=currentStep+k
	else:
		newStep=A*newStep
		for a in range(0,len(newStep)):
			#print newStep.item(a)
			#print addNewPoint(a*h,currentStep,newStep.item(a))
			addTupleToList(addNewPoint(a*h,currentStep,newStep.item(a)),solutionList)
			currentStep=currentStep+k


showList(solutionList)
Graph3DSolution(solutionList,"Forward Time Center Space : Heat Equation " + "\nh:" + str(h) + " k:" + str(k) +" v:"+ str(V) + " D:" + str(D) ,"x","t","u")




