from plot import *

def f(xnminus1,xn,yn,an):
	if(xn<=0):
		return ((an/(1-xn)) +yn)
	elif ( xn>0 and xn<(an+yn) and xnminus1<=0):
		return (an+yn)
	elif(xn>=(an+yn) or xnminus1 > 0):
		return -1
	else:
		raise Exception("Problem")
#two periodic

def alpha(a0,a1,n):
	if(n%2==0):
		return a0
	else:
		return a1
'''
def algo(x0,x1,y0,a0,a1,sigma,mew,n):
	title="x0=" + str(x0) + " x1=" + str(x1) + " " + " y0 = " + str(y0) + " a0 =" + str(a0) + " a1 = " + str(a1) + " sigma " + str(sigma) + " mew= " + str(mew) + " n=" + str(n)+ ".png" 

	xList=[]
	yandxList=[]
	yList=[]
	xList.append((0,x0))
	xList.append((1,x1))
	yList.append((0,y0))
	for currentNumber in range(1,n+1):
		xnminus1=xList[-2][1]
		x0=xList[-1][1]
		y0=yList[-1][1]
		xn1=f(xnminus1,x0,y0,alpha(a0,a1,currentNumber))
		yn1=y0 - mew*(x0+1)+ mew*sigma
		xList.append((currentNumber+1,xn1))
		yList.append((currentNumber, yn1))
		yandxList.append((xn1,yn1))
	Graph2DSolutions(xList,"n","xn", "xPLot " +title)
	Graph2DSolutions(yList,"n","yn","yPlot " +title)
	Graph2DSolutions(yandxList,"xn","yn",title)
	'''
'''
def algo(x0,x1,y0,alpha,sigma,mew,n):
	title="x0=" + str(x0) + " x1=" + str(x1) + " " + " y0 = " + str(y0) + " alpha =" + str (alpha) + " sigma " + str(sigma) + " mew= " + str(mew) + " n=" + str(n)+ ".png" 

	xList=[]
	yList=[]
	yandxList=[]
	xList.append((0,x0))
	xList.append((1,x1))
	yList.append((0,y0))
	for currentNumber in range(1,n+1):
		xnminus1=xList[-2][1]
		x0=xList[-1][1]
		y0=yList[-1][1]
		xn1=f(xnminus1,x0,y0,alpha)
		yn1=y0 - mew*(x0+1)+ (mew*sigma)
		xList.append((currentNumber+1,xn1))
		yList.append((currentNumber, yn1))
		yandxList.append((xn1,yn1))
	Graph2DSolutions(xList,"n","xn", "xPLot " +title)
	Graph2DSolutions(yList,"n","yn","yPlot " +title)
	Graph2DSolutions(yandxList,"xn","yn",title)
'''
'''
Used for scatter2D
def algo(x0,x1,y0,a0,a1,sigma,mew,n):
	title="x0=" + str(x0) + " x1=" + str(x1) + " " + " y0 = " + str(y0) + " a0 =" + str(a0) + " a1 = " + str(a1) + " sigma " + str(sigma) + " mew= " + str(mew) + " n=" + str(n)+ ".png" 

	xList=[]
	yandxList=[]
	yList=[]
	nlistX=[]
	nlistY=[]
	nlistX.append(0)
	nlistX.append(1)
	nlistY.append(0)
	xList.append(x0)
	xList.append(x1)
	yList.append(y0)
	for currentNumber in range(1,n+1):
		xnminus1=xList[-2]
		x0=xList[-1]
		y0=yList[-1]
		xn1=f(xnminus1,x0,y0,alpha(a0,a1,currentNumber))
		yn1=y0 - mew*(x0+1)+ mew*sigma
		nlistX.append(currentNumber+1)
		nlistY.append(currentNumber)
		xList.append(xn1)
		yList.append(yn1)
	Scatter2D(nlistX,xList,"xPlot "+title,"n","xn",4900,5000,-20,20)
	Scatter2D(nlistY,yList,"yPlot" +title,"n","yn",4900,5000,-20,20)
'''

'''

def sigmaDec(s0,s1,n):
	if(n%2==0):
		return s0
	else:
		return s1



def algo(x0,x1,y0,alpha,s0,s1,mew,n):
	title="x0=" + str(x0) + " x1=" + str(x1) + " " + " y0 = " + str(y0) + " alpha =" + str(alpha) + " sigma0= " + str(sigma0) + " sigma1 = "+ str(sigma1) + " mew= " + str(mew) + " n=" + str(n)+ ".png" 

	xList=[]
	yandxList=[]
	yList=[]
	nlistX=[]
	nlistY=[]
	nlistX.append(0)
	nlistX.append(1)
	nlistY.append(0)
	xList.append(x0)
	xList.append(x1)
	yList.append(y0)
	for currentNumber in range(1,n+1):
		xnminus1=xList[-2]
		x0=xList[-1]
		y0=yList[-1]
		xn1=f(xnminus1,x0,y0,alpha)
		yn1=y0 - mew*(x0+1)+ mew*(sigmaDec(s0,s1,currentNumber))
		nlistX.append(currentNumber+1)
		nlistY.append(currentNumber)
		xList.append(xn1)
		yList.append(yn1)
	Scatter2D(nlistX,xList,"xPlot "+title,"n","xn")
	Scatter2D(nlistY,yList,"yPlot" +title,"n","yn")
'''



'''
algo(.1,.2,.7,5.7,5.8,-.15,.001,6000)
algo(.1,.2,.7,5.7,5.8,.15,.001,6000)
algo(.1,.2,.7,5.7,5.8,5.15,.001,6000)
algo(.1,.2,.7,5.7,5.8,-5.15,.001,6000)




algo(.1,.2,.7,4.7,3.8,-.15,.001,6000)
algo(.1,.2,.7,4.7,3.8,.15,.001,6000)
algo(.1,.2,.7,4.7,3.8,5.15,.001,6000)
algo(.1,.2,.7,4.7,3.8,-5.15,.001,6000)


algo(.1,.2,.7,5.7,4.2,-15,.001,6000)
algo(.1,.2,.7,5.7,4.2,.15,.001,6000)
algo(.1,.2,.7,5.7,4.2,-5.15,.001,6000)
algo(.1,.2,.7,5.7,4.2,5.15,.001,6000)
'''




def algo(x0,x1,y0,a0,a1,sigma,mew,n):
	title="x0=" + str(x0) + " x1=" + str(x1) + " " + " y0 = " + str(y0) + " a0 =" + str(a0) + " a1 = " + str(a1) + " sigma " + str(sigma) + " mew= " + str(mew) + " n=" + str(n)+ ".png" 

	xList=[]
	yandxList=[]
	yList=[] 
	yandxList.append((x0,y0))
	xList.append((0,x0))
	xList.append((1,x1))
	yList.append((0,y0))
	for currentNumber in range(1,n+1):
		xnminus1=xList[-2][-1]
		x0=xList[-1][-1]
		y0=yList[-1][-1]
		xn1=f(xnminus1,x0,y0,alpha(a0,a1,currentNumber))
		yn1=y0 - mew*(x0+1)+ mew*sigma
		xList.append((currentNumber,xn1))
		yList.append((currentNumber,yn1))
		yandxList.append((xn1,yn1))
	Graph2DSolutions(xList,"xPlot "+title,"n","xn",4600,5000,-20,20)
	Graph2DSolutions(yList,"yPlot" +title,"n","yn",4600,5000,-20,20)
	#Graph2DSolutions(yList,"yn vs xn" +title,"xn","yn",0,5000,-20,20)
	xList=[]
	yList=[]
	yandxList=[]




#Done with Dr. Radin
#algo(.1,.2,.7,5.2,5.4,5.6,.001,8000)
#algo(.1,.2,.7,5.3,5.7,.1,.001,8000)
#algo(.1,.2,.7,5.1,5.8,1.4,.001,8000)
#algo(.1,.2,.7,5.03,5.9,3,.001,8000)
#algo(.1,.2,.7,5.12,5.5,4,.001,8000)
#algo(.1,.2,.7,5.6,5.9,5.2,.001,8000)
#algo(.1,.2,.7,6.2,5.1,.003,.001,8000)
#algo(.1,.2,.7,5.4,6.7,.000003,.001,8000)
#algo(.1,.2,.7,5.1,4.9,5.5,.001,8000)
#algo(.1,.2,.7,5.1,4.2,4.3,.001,8000)
#algo(.1,.2,.7,4.3,5.2,3,.001,8000)
#algo(.1,.2,.7,3.1,5.3,.5,.001,8000)
#algo(.1,.2,.7,5.7,3.1,.0001,.001,8000)
#algo(.1,.2,.7,5.7,2.5,.0000001,.001,8000)
#algo(.1,.2,.7,4.2,5.7,.15,.001,8000)
#algo(.1,.2,.7,5.7,4.2,.01,.001,8000)
#algo(.1,.2,.7,5.6,4.3,.15,.001,8000)
#algo(.1,.2,.7,5.6,4.3,5.15,.001,8000)
#algo(.1,.2,.7,5.8,4.1,5.15,.001,8000)
#algo(.1,.2,.7,2.8,4.7,5.15,.001,8000)
#algo(.1,.2,.7,4.8,3.9,5.15,.001,8000)
#algo(.1,.2,.7,4.7,3.8,5.15,.001,8000)
#algo(.1,.2,.7,4.9,4.2,5.15,.001,8000)
#algo(.1,.2,.7,5.6,4.3,5.15,.001,8000)
#start of good
#algo(.1,.2,.7,4.2,3.8,.1,.001,8000)
#algo(.1,.2,.7,5.6,4.1,.15,.001,8000)
#algo(.1,.2,.7,5.2,3.7,.15,.001,8000)
#algo(.1,.2,.7,4.7,3.2,.15,.001,8000)
#algo(.1,.2,.7,4.3,2.8,.15,.001,8000)
#algo(.1,.2,.7,3.0,4.5,.15,.001,8000)
'''
#additional plots
algo(.1,.2,.7,6,4.5,.15,.001,8000)
algo(.1,.2,.7,5,3.5,.15,.001,8000)
algo(.1,.2,.7,4.5,3,.15,.001,8000)
algo(.1,.2,.7,6.2,5.1,.003,.001,8000)
algo(.1,.2,.7,5.4,6.7,.000003,.001,8000)
algo(.1,.2,.7,5.4,3.1,.0001,.001,8000)
algo(.1,.2,.7,5.7,2.5,.0000001,.001,8000)
'''
'''
algo(.1,.2,.7,4.1,3,.15,.001,8000)
algo(.1,.2,.7,3.9,3,.15,.001,8000)
algo(.1,.2,.7,4.7,3,.15,.001,8000)
algo(.1,.2,.7,4.9,3,.15,.001,8000)
algo(.1,.2,.7,5.2,3.2,.15,.001,8000)
algo(.1,.2,.7,4.8,3.3,.15,.001,8000)
algo(.1,.2,.7,4.8,4,.15,.001,8000)
algo(.1,.2,.7,5.3,3.2,.15,.001,8000)
algo(.1,.2,.7,7,4.2,.15,.001,8000)
algo(.1,.2,.7,8,4.2,.15,.001,8000)
'''
#algo(.1,.2,.7,4.5,3,.15,.001,8000)





'''
algo(.1,.2,.7,4.5,3,.01,.15,8000)
algo(.1,.2,.7,4.5,3,.01,.1,8000)
algo(.1,.2,.7,4.5,3,.01,.01,8000)
algo(.1,.2,.7,4.5,3,.01,.45,8000)
algo(.1,.2,.7,4.5,3,.0001,.45,8000)
algo(.1,.2,.7,4.5,3,.000001,.45,8000)
algo(.1,.2,.7,4.5,3,.25,.45,8000)
algo(.1,.2,.7,4.5,3,.35,.45,8000)
'''
'''
algo(.1,.2,.7,5.2,5.1,.15,.001,8000)
algo(.1,.2,.7,5.2,5.1,.1,.001,8000)
algo(.1,.2,.7,5.2,5.1,.01,.001,8000)
algo(.1,.2,.7,5.2,5.1,.0001,.001,8000)
algo(.1,.2,.7,5.2,5.1,.000001,.001,8000)
algo(.1,.2,.7,5.2,5.1,.00000001,.001,8000)
algo(.1,.2,.7,5.2,5.1,.25,.001,8000)
algo(.1,.2,.7,5.2,5.1,.35,.001,8000)
algo(.1,.2,.7,5.2,5.1,.45,.001,8000)

algo(.1,.2,.7,5.2,5.1,.55,.001,8000)
algo(.1,.2,.7,5.2,5.1,.65,.001,8000)
algo(.1,.2,.7,5.2,5.1,.75,.001,8000)
algo(.1,.2,.7,5.2,5.1,.85,.001,8000)

'''
'''
1$
algo(.1,.2,.7,5.6,4.7,.75,.001,8000)
algo(.1,.2,.7,5.6,4.7,.65,.001,8000)
algo(.1,.2,.7,5.6,4.7,.55,.001,8000)
algo(.1,.2,.7,5.6,4.7,.45,.001,8000)
algo(.1,.2,.7,5.6,4.7,.35,.001,8000)
algo(.1,.2,.7,5.6,4.7,.25,.001,8000)
algo(.1,.2,.7,5.6,4.7,.15,.001,8000)
algo(.1,.2,.7,5.6,4.7,.05,.001,8000)
algo(.1,.2,.7,5.6,4.7,.00005,.001,8000)
algo(.1,.2,.7,5.6,4.7,.75,.000015,8000)
algo(.1,.2,.7,5.6,4.7,.75,.00000015,8000)
algo(.1,.2,.7,5.6,4.7,.75,.000000000005,8000)
'''
'''
algo(.1,.2,.7,4.5,3,.15,.001,8000)
algo(.1,.2,.7,4.4,3,.15,.001,8000)
algo(.1,.2,.7,4.3,3,.15,.001,8000)
algo(.1,.2,.7,4.2,3,.15,.001,8000)
algo(.1,.2,.7,4.1,3,.15,.001,8000)
algo(.1,.2,.7,4,3,.15,.001,8000)
algo(.1,.2,.7,3.9,3,.15,.001,8000)

algo(.1,.2,.7,4.5,3,.15,.001,8000)
algo(.1,.2,.7,4.6,3,.15,.001,8000)
algo(.1,.2,.7,4.7,3,.15,.001,8000)
algo(.1,.2,.7,4.8,3,.15,.001,8000)
algo(.1,.2,.7,4.9,3,.15,.001,8000)
algo(.1,.2,.7,5,3,.15,.001,8000)
'''
'''
algo(.1,.2,.7,4.5,3.5,.15,.001,8000)
algo(.1,.2,.7,4.4,3.5,.15,.001,8000)
algo(.1,.2,.7,4.3,3.5,.15,.001,8000)
algo(.1,.2,.7,4.2,3.5,.15,.001,8000)
algo(.1,.2,.7,4.1,3.5,.15,.001,8000)
algo(.1,.2,.7,4,3.5,.15,.001,8000)
algo(.1,.2,.7,3.9,3.5,.15,.001,8000)

algo(.1,.2,.7,4.5,3.5,.15,.001,8000)
algo(.1,.2,.7,4.6,3.5,.15,.001,8000)
algo(.1,.2,.7,4.7,3.5,.15,.001,8000)
algo(.1,.2,.7,4.8,3.5,.15,.001,8000)
algo(.1,.2,.7,4.9,3.5,.15,.001,8000)
algo(.1,.2,.7,5,3.5,.15,.001,8000)
'''

'''
algo(.1,.2,.7,5,3.5,.15,.001,8000)
algo(.1,.2,.7,5.1,3.5,.15,.001,8000)
algo(.1,.2,.7,5.2,3.5,.15,.001,8000)
algo(.1,.2,.7,5.3,3.5,.15,.001,8000)
algo(.1,.2,.7,5.4,3.5,.15,.001,8000)
algo(.1,.2,.7,5.5,3.5,.15,.001,8000)
algo(.1,.2,.7,5.6,3.5,.15,.001,8000)

algo(.1,.2,.7,5.7,3.5,.15,.001,8000)
algo(.1,.2,.7,5.8,3.5,.15,.001,8000)
'''
#1
'''
algo(.1,.2,.7,4.5,3,.15,.001,8000)
algo(.1,.2,.7,4.7,3.2,.15,.001,8000)
algo(.1,.2,.7,5,3.5,.15,.001,8000)
'''
'''
algo(.1,.2,.7,4.6,3,.15,.001,8000)
algo(.1,.2,.7,4.7,3,.15,.001,8000)
algo(.1,.2,.7,4.8,3,.15,.001,8000)
algo(.1,.2,.7,4.9,3,.15,.001,8000)
'''
'''
algo(.1,.2,.7,4.4,3,.15,.001,8000)
algo(.1,.2,.7,4.3,3,.15,.001,8000)
algo(.1,.2,.7,4.2,3,.15,.001,8000)
algo(.1,.2,.7,4.1,3,.15,.001,8000)
algo(.1,.2,.7,4.0,3,.15,.001,8000)
'''
'''
algo(.1,.2,.7,5.6,5.7,.15,.001,8000)
algo(.1,.2,.7,5.6,5.7,.1,.001,8000)
algo(.1,.2,.7,5.6,5.7,.01,.001,8000)
algo(.1,.2,.7,5.6,5.7,.001,.001,8000)
algo(.1,.2,.7,5.6,5.7,.0001,.001,8000)
algo(.1,.2,.7,5.6,5.7,.000001,.001,8000)
'''
algo(.1,.2,.7,5.6,5.7,.15,.001,8000)
algo(.1,.2,.7,5.6,5.7,.2,.001,8000)
algo(.1,.2,.7,5.6,5.7,.3,.001,8000)
algo(.1,.2,.7,5.6,5.7,.4,.001,8000)
algo(.1,.2,.7,5.6,5.7,.5,.001,8000)
algo(.1,.2,.7,5.6,5.7,.6,.001,8000)
algo(.1,.2,.7,5.6,5.7,.7,.001,8000)
#ocs occured colorful graphs
'''
algo(.1,.2,.7,5.7,5.8,.15,.001,8000)
algo(.1,.2,.7,5.7,5.8,5.15,.001,8000)
algo(.1,.2,.7,5.7,5.8,-5.15,.001,8000)




algo(.1,.2,.7,4.7,3.8,-.15,.001,8000)
algo(.1,.2,.7,4.7,3.8,.15,.001,8000)
algo(.1,.2,.7,4.7,3.8,5.15,.001,8000)
algo(.1,.2,.7,4.7,3.8,-5.15,.001,8000)


algo(.1,.2,.7,5.7,4.2,-15,.001,8000)
algo(.1,.2,.7,5.7,4.2,.15,.001,8000)
algo(.1,.2,.7,5.7,4.2,-5.15,.001,8000)
algo(.1,.2,.7,5.7,4.2,5.15,.001,8000)
algo(.1,.2,.7,4.5,3,.15,.001,8000)
'''
'''
algo(.1,.2,.7,5.5,5.7,-.15,.001,10000)
algo(.1,.2,.7,4.8,4.6,-.15,.001,10000)
algo(.1,.2,.7,4.6,5.7,-.15,.001,10000)
algo(.1,.2,.7,5.7,4.6,-.15,.001,10000)
'''
#algo(.1,.2,.7,4.8,-.003,.0001,10000)

#algo(.8,.1,.2,5.3,-.15,.001,100)
#algo(.1,.01,.4,5.3,-.15,.001,100)
#algo(1.2,1.1,.9,5.3,-.15,.001,100)

#around 5.3
