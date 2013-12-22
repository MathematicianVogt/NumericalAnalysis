package one;

import java.util.Scanner;

public class nDifference {
public static double functionX(double xo)
{
	
	return Math.pow(xo, 3)*Math.cos(xo);
	//return Math.pow(2, xo) +Math.sin(xo);
	//return xo+Math.exp(xo)
	//return Math.log(xo);
	
}
	
public static void main(String[] args)
{	Scanner done=new Scanner(System.in);
	
	



	System.out.println("h");
	double h = done.nextDouble();
	System.out.println("xo");
	double xo=done.nextDouble();
	double[] n1 = new double[4];
	double[] n2 = new double[3];
	double[] n3= new double[2];
	double[] n4=new double[1];
	
	for(int i=0; i<n1.length;i++)
	{
	    n1[i]=(int)(((functionX(xo + (h/(2^i)))-functionX(xo))/(h/(2^i)))*10000.0)/10000.0;
	    
	    
	}
	/*for(double t: n1)
    {
    	System.out.println(t);
    	
    }
//	*/
	for(int x=0; x<n1.length-2;x++)
	    {n2[x]=((int)(n1[x+1]+ (n1[x+1]-n1[x])*10000))/10000.0;
	    }
	for(int x=0; x<n2.length-2;x++)
		 {n3[x]=((int)(n2[x+1]+ (n2[x+1]-n2[x])*10000))/10000.0;
		 }
	 n4[0]=((int)(n3[1]+ (n3[1]-n3[0])*10000))/10000.0;
	 
	 for (double i: n1)
	 {
		 
		 System.out.println(i);
	 }
	
	
	
}
	
}
