import Data.Ratio
derv f a deltax = ((f (a+deltax))-(f a))/deltax :: Rational

getDerv f a deltax = fromRational (derv f a deltax)