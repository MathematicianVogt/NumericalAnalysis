package one;

import java.util.Scanner;

public class trapezoidIntegration {

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
double x1=done.nextDouble();
double area=((x1-x0)/2)*(function(x0)+function(x1));
System.out.println(area);
	
	
}

}
