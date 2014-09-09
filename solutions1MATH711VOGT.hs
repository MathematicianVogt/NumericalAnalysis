import Data.Ratio
--Ryan Vogt
--MATH 711 Source Code


--Herons method, check if the next step is on the same order as the old itteration.
--If so solution is found to order epsilon
--else recurse with the next value as the starting
herons :: (Num a,Fractional a, Ord a)=>a->a->a->a
herons c x0 epsilon = if((abs (x1-x0))<epsilon)
							then x1
							else herons c x1 epsilon
							where 
								x1 = (1/2)*(x0 +(c/x0))

--Using this in Newtons method to approximate f'(a)
centerDifference :: (Num a, Fractional a)=> (a->a)->a->a->a
centerDifference f a h = ((f (a+h))-(f (a-h)))/(2*h)

--Solving the equation f(x)=0 with newtons method.
newtonsMethod :: (Num a, Fractional a, Ord a)=>(a->a)->a->a->a->a
newtonsMethod f x0 h epsilon = if( (abs (x1-x0))<epsilon )
								then x1
								else newtonsMethod f x1 h epsilon
								where 
									fPrime=centerDifference f x0 h
									x1=x0-((f x0)/fPrime)
--Divides a grid from a to b in steps of h. Going to use for trapezoid rule
makeGridx :: (Enum a,Num a, Fractional a)=>a->a->a->[a]
makeGridx a b h =[a,(a+h)..b]


--Finds the integral with the use of trapezoid method
trapezoidIntegration ::(Fractional a, Num a)=>(a->a)->[a]->a->a
trapezoidIntegration f (x0:(x1:xn)) h =(h/2)*(integralSum f (x0:(x1:xn)))

--Helper function for integration, evalutes the sum over the grid
integralSum::(Num a, Fractional a)=>(a->a)->[a]->a
integralSum f (x0:(x1:xs)) = (f x0) + (f x1) + (integralSum f (x1:xs))
integralSum f [x1] =0

richardsonExtrapolation ::(Enum a,Fractional a)=>(a->a)->a->a->a->a
richardsonExtrapolation f a b h = (4*(trapezoidIntegration f (makeGridx a b (h/2)) (h/2)) - (trapezoidIntegration f (makeGridx a b h) h))/3


centerDifferenceSecondDerivative :: (Fractional a)=>(a->a)->a->a->a
centerDifferenceSecondDerivative f a h = ((f (a+h)) -2*(f a) + (f (a-h)))/(h^2)

forwardDifferenceSecondDerivative :: (Fractional a)=>(a->a)->a->a->a
forwardDifferenceSecondDerivative f a h = ((f (a+(2*h))) -2*(f (a+h)) + (f a))/(h^2)


backwardsDifferenceSecondDerivative :: (Fractional a)=>(a->a)->a->a->a
backwardsDifferenceSecondDerivative f a h = ((f a) -2*(f (a-h)) + (f (a-2*h)))/(h^2)



main = do 
	putStrLn ("Answer 1.1: " ++ ( show (herons 10 2 0.01)) ++"\n")
	putStrLn ("Answer 1.2: " ++ ( show (newtonsMethod (\x->(x^3 -(2*x)-5)) 2 0.01 0.0001)) ++"\n")
	putStrLn ("Answer 1.3 a: " ++ ( show (newtonsMethod (\x->x^3-x) (1/(sqrt 3)) 0.001 0.0000001)) ++"\n")
	putStrLn ("Answer 1.3 b: " ++ ( show (newtonsMethod (\x->x^3-x) (1/(sqrt 5)) 0.00001 0.0000001)) ++"\n")
	putStrLn ("Answer 1.4 b: " ++ ( show (trapezoidIntegration (\x->(exp x)) (makeGridx 0 0.5 0.25) 0.25)) ++"\n")
	putStrLn ("Answer 1.4 c, h=.5: " ++ ( show (richardsonExtrapolation (\x->(exp x)) 0 0.5 0.5)) ++"\n")
	putStrLn ("Answer 1.4 c, h=.25: " ++ ( show (richardsonExtrapolation (\x->(exp x)) 0 0.5 0.25)) ++"\n")
	putStrLn ("Answer 1.5 center, h=.1 : " ++ ( show (centerDifferenceSecondDerivative (\x->(cos x)) 0.6 0.1)) ++"\n")
	putStrLn ("Answer 1.5 forward, h=.1 : " ++ ( show (forwardDifferenceSecondDerivative (\x->(cos x)) 0.6 0.1)) ++"\n")
	putStrLn ("Answer 1.5 backwords, h=.1 : " ++ ( show (backwardsDifferenceSecondDerivative (\x->(cos x)) 0.6 0.1)) ++"\n")
	putStrLn ("Answer 1.5 center, h=.05 : " ++ ( show (centerDifferenceSecondDerivative (\x->(cos x)) 0.6 0.05)) ++"\n")
	putStrLn ("Answer 1.5 forward, h=.05 : " ++ ( show (forwardDifferenceSecondDerivative (\x->(cos x)) 0.6 0.05)) ++"\n")
	putStrLn ("Answer 1.5 backwords, h=.05 : " ++ ( show (backwardsDifferenceSecondDerivative (\x->(cos x)) 0.6 0.05)) ++"\n")
	putStrLn ("Answer 1.5 center, h=.001 : " ++ ( show (centerDifferenceSecondDerivative (\x->(cos x)) 0.6 0.001)) ++"\n")
	putStrLn ("Answer 1.5 forward, h=.001 : " ++ ( show (forwardDifferenceSecondDerivative (\x->(cos x)) 0.6 0.001)) ++"\n")
	putStrLn ("Answer 1.5 backwords, h=.001 : " ++ ( show (backwardsDifferenceSecondDerivative (\x->(cos x)) 0.6 0.001)) ++"\n")
	






