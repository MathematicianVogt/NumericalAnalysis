from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#x = np.arange(-5, 5, 0.25)
#y = np.arange(-5, 5, 0.25)
x=[]
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
y=[]
y.append(2)
y.append(2)
y.append(3)
y.append(4)
y.append(5)

X,Y= np.meshgrid(x,y)
Z = []
Z.append(6)
Z.append(2)
Z.append(3)
Z.append(4)
Z.append(5)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
print Z

plt.show()

