import math
class QuadSolver:
	def __init__(self,a,b,c):
		self.a=float(a)
		self.b=float(b)
		self.c=float(c)
		self.algo(self.a,self.b,self.c)

	def algo(self,a,b,c):
		det=math.pow(math.pow(b,2)-4*a*c,.5)
		if(det(a,b,c)>0):
			root1= lambda a,b,c:(-b+math.pow(math.pow(b,2)-4*a*c,.5)/(2*a)
			root2= lambda a,b,c:(-b+math.pow(math.pow(b,2)-4*a*c,.5)
		elif(det(a,b,c)==0)
			root=-b/(2*a)
		else:
			pass
		return root
