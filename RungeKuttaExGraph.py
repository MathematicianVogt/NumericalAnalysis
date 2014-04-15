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
		currentXtime=x+xh
		for t in range(startZ,endZ,zh):
			currentZtime=t+zh
			Algo(xList,zList,z0List,float(currentXtime),float(currentZtime))

def Algo(xList,zList,z0List,currentX,currentZ):
		z0=10.0
		t=SystemSolver("t,x,y,z","(1.0/" +str(currentX) + ")*" + "x*(1-x),2*y*(1-(y/((1-.5)*x +.5))) -.5*z, (1/"+ str(currentZ) +")*z*(1-(z/(1*y)))",".99,.74625," +str(z0),.001,100,2000)
		y=t.SolveSystem()
		if(y[-1]>0):
			xList.append(currentX)
			zList.append(currentZ)
			z0List.append(z0)
		else:
			a=0.0
			b=8.0
			while(float(b-a)>.02):
				#print "HERE"
				middle=float((a+b))/2.0
				#print str(middle)
				z0=middle
				t=SystemSolver("t,x,y,z", "(1.0/" +str(currentX)+ ")*" + "x*(1-x),2*y*(1-(y/((1-.5)*x +.5))) -.5*z, (1/"+ str(currentZ) +")*z*(1-(z/(1*y)))",".99,.74625,"+str(z0),.001,100,2000)
				y=t.SolveSystem()
				if(y[-1]>0):
					a=middle
				else:
					b=middle
			print "Done z0 has been found for " + str(z0)		
			xList.append(currentX)
			zList.append(currentZ)
			z0List.append(z0)


xTimeLoop(1,4,.25,1,11,1,xTime,zTime,z0)
xTimeLoop(1,4,.25,1,21,2,xTime,zTime,z0)
xTimeLoop(1,4,.25,1,41,4,xTime,zTime,z0)
xTimeLoop(1,11,1,1,11,1,xTime,zTime,z0)
xTimeLoop(1,11,1,1,21,2,xTime,zTime,z0)
xTimeLoop(1,11,1,1,41,4,xTime,zTime,z0)
xTimeLoop(1,21,2,1,11,1,xTime,zTime,z0)
xTimeLoop(1,21,2,1,21,2,xTime,zTime,z0)
xTimeLoop(1,21,2,1,41,4,xTime,zTime,z0)
zero=[]

for t in range(0,len(z0)):
	zero.append(0)


X,Y=np.meshgrid(xTime,zTime)
fig = plt.figure()
Z=z0
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xTime, zTime, z0)
ax.set_xlabel('x-timescale')
ax.set_ylabel('z-timescale')
ax.set_zlabel('z0')
plt.show()
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=10, cstride=10)
ax.set_xlabel('x-timescale')
ax.set_ylabel('z-timescale')
ax.set_zlabel('z0')
plt.show()