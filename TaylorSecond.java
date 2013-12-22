import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;


public class TaylorSecond {
	
	
	public double function(double t ,double y)
	{
		
		return (1/(Math.pow(t, 2)))*(Math.sin(2*t) -2*t*y);
		//return -y + t*(Math.pow(y, .5));
		//return (1+t)/(1+y);
		//return Math.exp(t-y);
		
		
	}
	public double functionD(double t, double y)
	{
		
		return (1/Math.pow(t, 2))*(2*Math.cos(2*t)-2*y)+(Math.sin(2*t)-2*t*y)*(-2/Math.pow(t, 3))-((2*t*(Math.sin(2*t)-2*t*y))/(Math.pow(t, 2))) ;
		//return Math.pow(y,.5)-(-y+t*Math.pow(y,.5))+ .5*t*Math.pow(y, -.5)*(-y +Math.pow(y,.5)*t);
		//return (1/(y+1))-((1+t)/Math.pow((1+y),2))*((1+t)/(1+y));
		//return Math.exp(t-y) - Math.exp(t-y)*Math.exp(t-y);
		
	}
	public String eulerAlgo()
	{	ArrayList<Double> inputFun = new ArrayList<Double>();
		ArrayList<Double> outputFun = new ArrayList<Double>();
		Scanner input = new Scanner(System.in);
		System.out.println("h");
		double h=input.nextDouble();
		System.out.println("a");
		double a =input.nextDouble();
		System.out.println("b");
		double b = input.nextDouble();
		System.out.println("IC");
		double IC = input.nextDouble();
		double n = (b-a)/h;
		double t = a;
		double w = IC;
		int counter=1;
		String finalstr="";
		
		inputFun.add(t);
		outputFun.add(w);
		
		for(int i=1; i<=n; i++)
		{
			
			w=w+(h*(function(t,w)+(h/2)*functionD(t,w)));
			t= a+(i*h);
			inputFun.add(t);
			outputFun.add(w);
			
		}
		Iterator<Double> it1 = inputFun.iterator();
		Iterator<Double> it2 = outputFun.iterator();
		while(it1.hasNext())
		{
			finalstr = finalstr + "Step " + counter + ":" + " x:" + it1.next() + " y:" + " " + it2.next() + "\n" ;
			counter++;
			
			
		}
		return finalstr;
	}
	public static void main (String[] args)
	{
		TaylorSecond go = new TaylorSecond();
		System.out.println(go.eulerAlgo());
		
		
	}

}
