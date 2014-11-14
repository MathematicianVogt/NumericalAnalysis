def generateCoeff(p1,p2):
	ck=[]
	maxNum=len(p1)+len(p2)-1
	for j in range(0,maxNum):
		cof=0
		for x in range(0,j):
			cof=cof +p1[x]*p2[len(p1)-x-1]
			print cof
			print "FINISHED"
		print "ADDING"
		ck.append(cof)
		
	ck[::-1]
	print ck
generateCoeff([1,1],[1,1])