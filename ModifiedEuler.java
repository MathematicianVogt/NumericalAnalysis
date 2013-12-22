import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;


public class ModifiedEuler {
	
	
	
	public double mainFunction(double t)
	{
		
		return Math.sqrt(4-3*Math.exp(-Math.pow(t, 2)));
		//return (2*t)/(1-2*t);
		
		
	}
	public double function(double t,double y)
	{
		return Math.cos(2*t)+Math.sin(3*t);
		//return 1+ (y/t);
		//return 1+Math.pow(t-y, 2);
		//return t*Math.exp(3*t)-2*y;
		//return Math.pow(t, 2);
		//return (Math.pow(y, 2)+y)/t;
		//return Math.sin(t)+Math.exp(-t);
		//return Math.pow(y/t, 2) + (y/t);
		
		//
		//return Math.pow(y/t, 2) + (y/t);	
		//return -t*y +(4*t)/y;
		//return (Math.pow(y, 2)+y)/t;
		//return (Math.pow(y, 2)/(1+t));
		//return (2-2*t*y)/(Math.pow(t, 2)+1);
		//return (1/(Math.pow(t, 2)))*(Math.sin(2*t) -2*t*y);
		//return -y + t*(Math.pow(y, .5));
		//return (1+t)/(1+y);
		//return Math.exp(t-y);
		
	}
	public String eulerAlgo()
	{	ArrayList<Double> inputFun = new ArrayList<Double>();
		ArrayList<Double> outputFun = new ArrayList<Double>();
		ArrayList<Double> mainfun = new ArrayList<Double>();
		Scanner input = new Scanner(System.in);
		String otherString="";
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
		mainfun.add(mainFunction(a));
		
		for(int i=1; i<=n; i++)
		{
			
			w=w+((h/2)*(function(t,w)+function(a+(i*h),w+h*function(t,w))));
			t= a+(i*h);
			inputFun.add(t);
			mainfun.add(mainFunction(t));
			outputFun.add(w);
			
		}
		Iterator<Double> it1 = inputFun.iterator();
		Iterator<Double> it2 = outputFun.iterator();
		Iterator<Double> it3 = mainfun.iterator();
		while(it1.hasNext())
		{	double point1 = it2.next();
			finalstr = finalstr + "Step " + counter + ":" + " x:" + it1.next() + " y:" + " " + point1 + "\n" ;
			counter++;
			double point=it3.next();
			otherString = otherString + "Real value: " + point + " Absolute error: " + Math.abs(point-point1) + "\n";
			
		}
		finalstr=finalstr+otherString;
		return finalstr;
	}
	
	
	
	public static void main(String[] args)
	{
		ModifiedEuler go = new ModifiedEuler();
		System.out.println(go.eulerAlgo());
		
		
	}

}
