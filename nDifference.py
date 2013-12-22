import math
    
def functionX(x):
    return math.log(x)
def differences():
        xo=float(raw_input("xo"))
        h=float(raw_input("h"))
        n=4
        n1=[0,0,0,0]
        n2=[0,0,0]
        n3=[0,0]
        n4=[0]
        
        for x in range(0,int(n)-1):
            n1[x]=((functionX(xo + (h/(2**x)))-functionX(xo))/(h/(2**x)))
            print n1
        for y in range(0,len(n1)-2):
            n2[x]=(int(n1[x+1]+ (n1[x+1]-n1[x]))*10000)/10000.0
            print n2
        for z in range(0,len(n2)-2):
            n3[x]=(int(n2[x+1]+ (n2[x+1]-n2[x]))*10000)/10000.0
            print n3
        n4=(int(n3[x+1]+ (n3[x+1]-n3[x]))*10000)/10000.0
        print n4
        
differences()
        