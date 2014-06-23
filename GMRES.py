from scipy import *
from numpy import *
import numpy as np
import math

class GMRES:
	def __init__(self,A,b,TOL,x):
	 	self.a=np.matrix(A)
	 	self.b=np.matrix(b).T
	 	self.x=np.matrix(x).T
	 	self.tol=TOL
	def Algo(self):
	 	
	 	A=self.a
		n=self.n
		B=self.b
		q1=B/np.linalg.norm(B,2)
		qn=[[]]
		vectorlist=[]
		
		for x in range(0,1000):
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
			yn=qn[[x]*A
			e=[1,0,0,0]
			b=np.linalg.norm(b-A*self.x)
			rn=h1*yn-b*e
			x=qn[x]*yn


		print str(x)






x=GMRES('[2 1 1; 1 2 1; 1 1 2]','[1,2,1]', .001, '[0,0,0]')
x.Algo()
