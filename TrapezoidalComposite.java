package one;

import java.util.Scanner;

public class TrapezoidalComposite {

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
double x0=Math.E;
double x1=Math.E +2;
double n=done.nextDouble();
double h=(x1-x0)/n;

double xi0=function(x0)+function(x1);
double xi1=0;
double xi2=0;

for(int i=1; i<n;i++)
{
	
double x=x0+(i*h);	

if(i%2==0)
{
xi2=xi2+function(x);	
	
}
else
{
	xi1=xi1+function(x);
	
}





	
	
}
double xi=(h*((xi0)+(2*xi2)+(4*xi1)))/3;
System.out.println(xi);
}
}