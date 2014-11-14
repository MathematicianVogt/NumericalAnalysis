import pylab 
import numpy
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np





def plotSolution():
	fig = plt.figure()
	ax=fig.gca(projection='3d')
	x=numpy.arange(0,300,1)
	y=numpy.arange(0,100,1)
	X,Y=numpy.meshgrid(x,y)
	z=numpy.sin(((math.pi)/100.0)*X)*numpy.sin(((math.pi)/100.0)*Y)
	ax.plot_surface(X,Y,z)
	pylab.ylim([0,100])
	pylab.xlim([0,300])
	plt.show()


def graph(x,v0):
	row=1
	tau=1
	sigma=1
	g=980
	posY=[]
	negY=[]
	for t in x:
		w=((row*tau*v0)/sigma)*math.pow(v0**2 +2*g*t,.5)
		y1=((2.0/3.0)*((sigma**2)/((row**2)*(tau**2)*(v0**2)*g)))*math.pow(w-1,.5)*(w+2) 
		y2=-((2.0/3.0)*((sigma**2)/((row**2)*(tau**2)*(v0**2)*g)))*math.pow(w-1,.5)*(w+2) 
		posY.append(y1)
		negY.append(y2)

	pylab.plot(x,posY, label="Positive Family")
	
	pylab.plot(x,negY,label="Negitive Family")
	pylab.legend()
	pylab.title("Characteristics for initital velocity " + str(v0))
	pylab.xlabel("x")
	pylab.ylabel("y")
	pylab.show()

#plotSolution()
x=numpy.arange(0,300,1)
graph(x,8.7)
graph(x,20.0)
graph(x,200.0)