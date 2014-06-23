import math
import pylab
import numpy

def discrete(x1,y1,a):
	xlist=[]
	ylist=[]
	x0=x1
	y0=y1
	for x in range(0,1001):
		xlist.append(x0)
		ylist.append(y0)
		xn=(3.0/5.0)*x0 +(4.0/5.0)*y0 -x0*(x0**2 + y0**2)
		yn=(-a/5.0)*x0 +(3.0/5.0)*y0 -y0*(x0**2 + y0**2)
		x0=xn
		y0=yn
	pylab.plot(xlist,ylist)
	pylab.show()

discrete(.1,.1,0.0)
discrete(.1,.1,2.0)
discrete(.1,.1,4.0)
discrete(.1,.1,6.0)