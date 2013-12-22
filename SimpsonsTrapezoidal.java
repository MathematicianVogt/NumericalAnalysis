package one;

import java.util.Scanner;

public class SimpsonsTrapezoidal {

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
double totalSum=0;

for(int j=0;j<=n;j++)
{
	totalSum=totalSum+function(x0+(j*h));
	
	
}



double area=(h/2)*(function(x0)+(2*totalSum) + function(x1));
System.out.println(area);
}

}