import java.util.Scanner;


public class adaptivequad {
public static double first;
public static double second;
public static double h;
public static Scanner in;

public static void set()
{
in=new Scanner(System.in);
first=in.nextDouble();
second=in.nextDouble();
h=(second-first)/2;

}
public static double function(double x)
{
	
	return (6*Math.cos(4*x)+4*Math.sin(6*x))*Math.pow(Math.E, x);
			
	//return x*Math.sin(4*x);
	//return x+4*Math.sin(4*x);
	//return Math.sin(x)+Math.cos(x);
	
}

public static void aQuad()
{
	double sum=(h/6)*(function(first)+ 4*(function(first+(h/2)))+ 2*(function(first+h)) + 4*function(first + (3*(h/2)))+ function(second));
	System.out.println("Sum " + sum);
}
public static void main(String[] args)
{
set();
aQuad();
	
}

}
