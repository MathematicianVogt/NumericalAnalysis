import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;


public class TaylorFourth {
	public double function(double t ,double y)
	{
		
		//return (1/(Math.pow(t, 2)))*(Math.sin(2*t) -2*t*y);
		return -y + t*(Math.pow(y, .5));
		//return (1+t)/(1+y);
		//return Math.exp(t-y);
		
		
	}
	public double functionD(double t, double y)
	{
		
		//return (1/Math.pow(t, 2))*(2*Math.cos(2*t)-2*y)+(Math.sin(2*t)-2*t*y)*(-2/Math.pow(t, 3))-((2*t*(Math.sin(2*t)-2*t*y))/(Math.pow(t, 2))) ;
		return Math.pow(y,.5)-(-y+t*Math.pow(y,.5))+ .5*t*Math.pow(y, -.5)*(-y +Math.pow(y,.5)*t);
		//return (1/(y+1))-((1+t)/Math.pow((1+y),2))*((1+t)/(1+y));
		//return Math.exp(t-y) - Math.exp(t-y)*Math.exp(t-y);
		
	}
	public double functionE(double t, double y)
	{
		return t*Math.pow(y, .5)-y-Math.pow(y, .5)-(t/2)*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y)+.5*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y)-.5*Math.pow(y, .5) -(t/4)*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y) +t;
		//return -(Math.pow(1+y, -2))*((1+t)*Math.pow(1+y, -1)) - 2*(1+t)*Math.pow(1+y, -3) +3*Math.pow(1+t, 3)*Math.pow(1+y, -5);	
		//return Math.exp(t-y)*(1-Math.exp(t-y))*(1-2*Math.exp(t-y));
	}
	public Double functionF(double t, double y)
	{
		return (3/2)*Math.pow(y,.5)+(t/2)*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y)-(t*Math.pow(y, .5)-y)-(1/2)*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y)-(1/4)*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y)+(t/4)*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y)-(1/4)*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y) +(1/4)*Math.pow(y, .5)+(t/8)*Math.pow(y, -.5)*(t*Math.pow(y, .5)-y)-(3/2)*t +(3/2);
		//return 2*(1+t)*(Math.pow(1+y, -4))-3*Math.pow(1+y, -3)+16*Math.pow(1+t, 2)*Math.pow(1+y, -5)-15*Math.pow(1+t, 4)*Math.pow(1+y, -7);
		//return Math.exp(t-y)*(1-Math.exp(t-y))*(1-2*Math.exp(t-y)) - 2*Math.pow((Math.exp(t-y)*(1-Math.exp(t-y))),2);
		
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
			
			w=w+(h*(function(t,w)+(h/2)*functionD(t,w) + (Math.pow(h, 2)/6)*functionE(t,w) + (Math.pow(h, 3)/24)*functionF(t,w)));
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
		TaylorFourth go = new TaylorFourth();
		System.out.println(go.eulerAlgo());
		
		
	}

}



