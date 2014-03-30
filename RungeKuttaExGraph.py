#Written by Ryan Vogt @ RIT
#Approximate to solution to N differentiation equations with initial conditions
#FIND EQUIL POINTS
import math
import pylab
from RungeKuttaExY import SystemSolver
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

xTime=[]
zTime=[]
z0=[]

def xTimeLoop(startX,endX,xh,startZ,endZ,zh,xList,zList,z0List):
	for x in range(startX,endX):
		currentXtime=x*xh
		for t in range(startZ,endZ,zh):
			currentZtime=t*zh
			Algo(xList,zList,z0List,currentX,currentZ)

def Algo(xList,zList,z0List,currentX,currentZ):
	SURVIAL_CONSTANT=10
	x=SystemSolver("t,x,y,z","-x*(1-x),2*y*(1-(y/((1-.5)*x +.5))) -.5*z, (1/18.7)*z*(1-(z/(1*y)))",".99,.74625,.74625",0,1000,100000)





fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.set_xlabel('x-timescale')
ax.set_ylabel('z-timescale')
ax.set_zlabel('z0')
plt.show()