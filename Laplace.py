	#Ryan Vogt
	#Computer Science and Applied Mathematics major at RIT
	#Numerical solution to laplces equation
class laplacesEquation:
	#condition dxN dyN >=3
	def __init__(self,x0,x1,y0,y1,dxN,dyN,tol,maxN,fxy,gxy):
		self.x0=float(x0)
		self.x1=float(x1)
		self.y0=float(y0)
		self.y1=float(y1)
		self.dxN=dxN
		self.dyN=dyN
		self.tol=float(tol)
		self.max=maxN
		self.xCor=[]
		self.yCor=[]
		self.zCor=[[]]
		self.fxy=fxy
		self.gxy=gxy
	def generateXMeshPoints(self,h):
		self.xCor.append(self.x0)
		for i in range(1,self.dxN):
			xi=self.x0+(i*h)
			self.append(xi)
	def generateKMeshPoints(self,k):
		self.yCor.append(self.y0)
		for i in range(1,self.dyN):
			yi=self.y0+(i*k)
			self.append(yi)
	def generateOmegas(self):
		wList=[]
		for i in range(1,self.dyN):
			for j in range(1,self.dxN):
				wList.append(0)
			

			self.zCor.append(wList)
			wList=[]



	def GaussSiedelFiniteDifference(self):
		h=(self.x1-self.x2)/self.dxN
		k=(self.y1-self.y0)/self.dyN
		self.generateOmegas()
		self.generateKMeshPoints()
		self.generateXMeshPoints()



	def generateSolution(self):
		pass

			
