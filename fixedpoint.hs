fixedPoint :: (Fractional a,Num a, Ord a) => (a -> a) -> a -> a -> a
fixedPoint f x0 epsilon = 	if((abs (x1-x0) ) < epsilon )
							then x1
							else fixedPoint f x1 epsilon
							where x1 = (f x0)