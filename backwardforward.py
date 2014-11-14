#Ryan Vogt
#Solving systems with a lower or upper triangular transformation
from scipy import *
from numpy import*
import scipy.linalg as s
import numpy.linalg as np
import math
b=mat('[2 4 6]').T
A=mat('[4 2 0; 4 4 2; 2 2 3]')
p,l,u=s.lu(A)



#Assuming A is lower triangular
def forward(A,b):
	p,l,u=s.lu(A)
	newB=b
	solutionList=[]
	for z in range(0,newB.shape[0]):
		mySum=0
		for j in range(0,z):
			mySum=mySum+ (l.item((z),j)*solutionList[j])
		xm=(newB.item(z)-mySum)/l.item(z,z)
		solutionList.append(xm)
	return mat(asarray(solutionList)).T
#Assuming A is upper triangular 
def backwards(A,b):
	p,l,u=s.lu(A)
	newB=b
	solutionList=[]
	for z in range(0,newB.shape[0]):
		mySum=0
		for j in range(0,z):
			mySum=mySum+ (u.item(z,z-j)*solutionList[z-1-j])
		xm=(newB.item(newB.shape[0]-1 -z)-mySum)/u.item(newB.shape[0]-1 -z,newB.shape[0]-1 -z)
		solutionList.append(xm)
	solutionList=solutionList[::-1]
	return mat(asarray(solutionList)).T

b=mat('[2 4 6]').T
A=mat('[4 2 0; 4 4 2; 2 2 3]')
p,l,u=s.lu(A)

c=forward(A,p*b)
d=backwards(A,c)
print "Solution using BWS FWS"
print d
print "Inverse solution"
print (np.inv(A)*b)




'''
Ryans-MacBook-Pro-4:NumericalAnalysis MathematicianVogt$ python backwardforward.py 
Solution using BWS FWS
[[ 1.]
 [-1.]
 [ 2.]]
Inverse solution
[[ 1.]
 [-1.]
 [ 2.]]
 '''