import numpy
import pylab
import math
a=-1.0
h=2.0/float(256)

tlist=[]
for x in range(1,256):
	if(a>=1):
		break
	tlist.append(a)
	a=a+h

for y in range(1,6):
	currentLegendre=numpy.polynomial.legendre.legvander(tlist, y)
	pylab.plot(tlist,currentLegendre)
pylab.ylim(-2, 2)
pylab.show()

