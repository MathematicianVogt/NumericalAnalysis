from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as pl
import numpy as np

'''
x=np.arange(1,2.1,.5)
y=np.arange(4,5.1,.5)
print y
print x
X,Y= np.meshgrid(x,y)
print X
print Y
Z=np.add(X+Y)
Axes3D.plot_surface(X,Y,Z)
'''
'''
x=(1,2,3)
y=(4,5,6)
z=1
ax.scatter(x,y,z)
plt.show()
'''
'''
x=([1,2,3,4,5])
y=([6,7,8,7,10])
z=([1,1,1,1,1])
ax.plot_surface(x,y,z)
plt.show()
'''
fig = pl.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
pl.show()
