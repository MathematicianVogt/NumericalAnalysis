from scipy import *
from numpy import *
import numpy as np
import math

class Arnoldi:
	#breaks A into QH(Q^T) with starting q1 B
	#just prints out coloumbs currently q1....qn, will be issue for large matrices.
	def __init__(self,A,N,B):
		self.a=mat(A)
		self.n=N
		self.b=mat(B).T
	def algo(self):
		A=self.a
		n=self.n
		B=self.b
		q1=B/np.linalg.norm(B,2)
		vectorlist=[]
		
		for x in range(0,n+1):
			#print str(q1)
			vectorlist.append(q1)
			v=A*vectorlist[x]
			#print str(v)
			for y in range(0,x):
				h=((vectorlist[y]).T)*v
				print str(h)
				v=v-(float(h.item(0))*vectorlist[y])
			h1=np.linalg.norm(v,2)
			q1=v/h1
		for x in vectorlist:
			print str(x)
x=Arnoldi('[1 0 2 3;-1 0 5 2;2 -2 0 0; 2 -1 2 0]',4,'[1.0,1.0,1.0,1]')
x.algo()

ex=mat('[1 .5 .333;.5 .333 .25; .333 .25 .20]')
ex1=mat('[0.0 0.0 .00003; 0.0 0.0 0.0; 0.0 0.0 0.0')
print str(linalg.cond(ex))
print str(linalg.norm(ex,2))















