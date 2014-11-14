#IMPLICT HEAT EQUATION

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
d_main_left = (1+2*r)*iden  # values that will go on main diagonal
d_sub_left = -r*iden     # values that will go on subdiagonal
d_super_left = -r*iden     # values that will go on superdiagonal
data_left = [d_sub_left, d_main_left, d_super_left]   # list of all the data
                  # which diagonal each vector goes into

d_main_right = (1-2*r)*iden  # values that will go on main diagonal
d_sub_right = r*iden     # values that will go on subdiagonal
d_super_right = r*iden     # values that will go on superdiagonal
data_right = [d_sub_right, d_main_right, d_super_right]   # list of all the data
diags = [-1,0,1]

Aright = l.spdiags(data_right,diags,Nx,Nx,format='csc')  # create the matrix
Aleft = l.spdiags(data_left,diags,Nx,Nx,format='csc')  # create the matrix


zeroVector=linspace(0,0,Nx)
realu0=matrix(zeroVector).T
zeroVector[0]=1
jumpu0=matrix(zeroVector).T

solutionList=[]

Aleft[(Aleft.shape[0]-1),-1]=(1+(2*r))
Aleft[(Aleft.shape[0]-1),-2]=-2*r

Aright[(Aright.shape[0]-1),-1]=(1-(2*r))
Aright[(Aright.shape[0]-1),-2]=2*r

#SET RIGHT BOUNDARY CONDITIONS
Aleft[0,0]=(1+2*r - ((4*V*r)/(2*V+h)))
Aleft[0,1]= -r -((r*h)/2*V+h) +((2*V*r)/(2*V+h))

Aright[0,0]=(1-2*r+((4*V*r)/(2*V+h)))
Aright[0,1]= (r+ ((r*h)/(2*V+h)) -((2*V*r)/(2*V +h)))





solutionVector=jumpu0
currentStep=0
while(currentStep<=t1):
	rightSol=(Aright.todense()*solutionVector)
	solutionVector=lin.inv(Aleft.todense())*rightSol
	if(currentStep==0):
		for a in range(0,len(realu0)):
			#print addNewPoint(a*h,currentStep,realu0.item(a))
			addTupleToList(addNewPoint(a*h,currentStep,realu0.item(a)),solutionList)
			currentStep=currentStep+k
	else:
		rightSol=(Aright.todense()*solutionVector)
		solutionVector=lin.inv(Aleft.todense())*rightSol
		for a in range(0,len(solutionVector)):
			#print newStep.item(a)
			#print addNewPoint(a*h,currentStep,newStep.item(a))
			addTupleToList(addNewPoint(a*h,currentStep,solutionVector.item(a)),solutionList)
			currentStep=currentStep+k


Graph3DSolution(solutionList,"Crank N. Implict : Heat Equation","x","t","u")

