from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import numpy as np


'''
When graphinh tuples in pylab!!!!!!

plt.scatter(*zip(*dataList))
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.savefig(title)
'''



def Graph3DSolution(dataList,title,xLabel,yLabel,zLabel):
	data = dataList



	x, y, z = zip(*data)
	z = map(float, z)
	grid_x, grid_y = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]
	grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')

	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.plot_surface(grid_x, grid_y, grid_z, cmap=plt.cm.Spectral)
	ax.set_xlabel(xLabel)
	ax.set_ylabel(yLabel)
	ax.set_zlabel(zLabel)
	ax.set_title(title)
	plt.show()
def Graph2DSolutions(dataList,title,xlabel,ylabel,xMin,xMax,yMin,yMax):
	plt.plot(*zip(*dataList))
	#plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.ylim([yMin,yMax])
	plt.xlim([xMin,xMax])
	plt.savefig(title)
	plt.clf()
def Scatter2D(xList,yList,title,xlabel,ylabel,xMin,xMax,yMin,yMax):
	plt.scatter(xList,yList,s=1,marker='.')
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.ylim([yMin,yMax])
	plt.xlim([xMin,xMax])
	plt.savefig(title)