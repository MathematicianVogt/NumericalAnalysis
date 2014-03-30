from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as pl
import numpy as np
import pylab

#case1
rx=[]
for x in range(1,11):
	rx.append(1/(x*.1))
print rx
y=(1,2,3,4,5,6,7,8,9,10)
z=(1,2,3,4,5,6,7,8,9,10)
fig = pl.figure()
ax = Axes3D(fig)
ax.scatter(rx,y,z)
pl.title("Case 1")
pl.savefig("Case1-3d.png")
pl.show()

pylab.plot(rx,y)
pylab.savefig("Case1-2d.png")
pylab.show()


#case2
rx=[]
for x in range(1,11):
	rx.append(1)
print rx
y=(.1,.2,.3,.4,.5,.6,.7,.8,.9,.10)
z=(.1,.2,.3,.4,.5,.6,.7,.8,.9,.10)
fig = pl.figure()
ax = Axes3D(fig)
ax.scatter(rx,y,z)
pl.title("Case 2")
pl.savefig("Case2-3d.png")
pl.show()

pylab.title("Case 2")
pylab.plot(rx,y)
pylab.savefig("Case2-2d.png")
pylab.show()

#case3
rx=[]
for x in range(1,11):
	rx.append(x*1.1)
print rx
y=(.1,.2,.3,.4,.5,.6,.7,.8,.9,.10)
z=(2,2,3,4,5,6,7,8,9,10)
fig = pl.figure()
ax = Axes3D(fig)
ax.scatter(rx,y,z)
pl.title("Case 3")
pl.savefig("Case3-3d.png")
pl.show()

pylab.title("Case 3")
pylab.plot(rx,y)
pylab.savefig("Case3-2d.png")
pylab.show()


#case4
rx=[]
for x in range(1,11):
	rx.append(x*.1)
print rx
y=(1,1,1,1,1,1,1,1,1,1)
z=(2,2,3,4,5,6,7,8,9,10)
fig = pl.figure()
ax = Axes3D(fig)
ax.scatter(rx,y,z)
pl.title("Case 4")
pl.savefig("Case4-3d.png")
pl.show()

pylab.title("Case 4")
pylab.plot(rx,y)
pylab.savefig("Case4-2d.png")
pylab.show()


