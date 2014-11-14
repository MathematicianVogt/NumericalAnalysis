def generateCoeff(p1,p2):
	ck=[]
	maxNum=len(p1)+2
	for j in range(0,maxNum+1):
		cof=0
		for x in range(0,j):
			cof=cof +p1[x]*p2[len(p1)-x-1]
			print cof
			print "FINISHED"
		print "ADDING"
		ck.append(cof)
		
	ck[::-1]
	print ck
def otherPoly(p1,p2):
	



def addaZero(mylist,numberOfZeros):
	final=[]
	for x in range(0,numberOfZeros):
		final.append(0)
	for i in range(0,len(mylist)):
		final.append(mylist[i])