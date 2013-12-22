import math
import parser
class romberg:
    def function(self,a,t):
       form = parser.expr(a).compile()
       x=t
       return eval(form)
    
    
    
    
z=romberg()
formula=raw_input("formula")
point=raw_input("point")
print str(z.function(str(formula), float(point)))
        