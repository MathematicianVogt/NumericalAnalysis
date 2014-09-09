def center(f,x0,h):
	return (f(x0+h)-(2*f(x0))+f(x0-h))/(h**2)


print str(center((lambda x:x**3),2,.000001))
