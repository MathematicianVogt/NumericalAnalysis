def horner(poly, x):
	acc = 0
	for c in reversed(poly):
		acc = acc * x + c
	print acc
horner([2,0,-3,2,1],2)