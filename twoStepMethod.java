import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;


public class twoStepMethod {
	
	public double function(double t, double y)
	{
		
		return 1-y;
		
	}
	public String twoAlgo()
	{
		
		ArrayList<Double> inputFun = new ArrayList<Double>();
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
		System.out.println("IC2");
		double IC2=input.nextDouble();
		double n = (b-a)/h;
		double t = a;
		double wi = IC;
		double wi1=IC2;
		double t1=t+h;
		double wi2=0;
		int counter=1;
		String finalstr="";
		
		inputFun.add(t);
		inputFun.add(t1);
		outputFun.add(wi);
		outputFun.add(wi1);
		t=t+2*h;
		for(int i=0; i<=n-2; i++)
		{
			
			wi2=4*wi1 -3*wi -2*h*function(t,wi);
			wi1=wi2;
			wi=wi1;
			inputFun.add(t);
			outputFun.add(wi);
			t= a+((3+i)*h);
			
			
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
	
	
	
	public static void main(String[] args)
	{
		
		twoStepMethod mine = new twoStepMethod();
		System.out.println(mine.twoAlgo());
	}
		
}
