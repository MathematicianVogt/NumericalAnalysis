package one;

import java.util.Scanner;
//trapezoid command
public class simpsonIntegration {

public static double function(double x)
{
	return (1/(x*Math.log(x)));
	//return (Math.pow(Math.sin(x), 2) -2*x*Math.sin(x)+1);
	//return x*Math.log(x+1);
	//return Math.pow(Math.cos(x), 2);
}
	
public static void main(String[] args)
{
Scanner done=new Scanner(System.in);
double x0=done.nextDouble();
double x2=done.nextDouble();
double h=(x2-x0)/2;
double x1=x0+h;
double area=(h/3)*(function(x0)+ 4*function(x1) + function(x2));
System.out.println(area);
	
	
}

}
