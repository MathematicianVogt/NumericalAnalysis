'''
Ryan Vogt
Forward Backward Difference Algo
'''
class Difference():
   
        
    def algo(self,xn,h):
        xh=xn+h
        print str(((self.function(xh)-self.function(xn))/h))
    
    def function(self,xn):
        return xn**2   
    
    
    
one=Difference()
point=raw_input("xn: ")
h=raw_input("h : ")
one.algo(float(point), float(h)) 