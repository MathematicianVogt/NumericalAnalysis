import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;


public class AdamVariable {
	double a;
	double b;
	double IC;
	double tol;
	double hmin;
	double hmax;
	ArrayList<Double> x;
	ArrayList<Double> y;
	ArrayList<ArrayList<Double>> hold;
	ArrayList<Double> finalX;
	ArrayList<Double> finalY;
	double q;
	String finalstr="";
	
	public AdamVariable()
	{ Scanner in = new Scanner(System.in);
		a=in.nextDouble();
		b=in.nextDouble();
		IC=in.nextDouble();
		tol=in.nextDouble();
		hmin=in.nextDouble();
		hmax=in.nextDouble();
		x = new ArrayList<Double>();
		y = new ArrayList<Double>();
		hold = new ArrayList<ArrayList<Double>>();
		finalX= new ArrayList<Double>();
		finalY = new ArrayList<Double>();
		
		
		
		
	}
	public ArrayList<ArrayList<Double>> rungeFourth(double h,double x0,double y0)
	{	
		hold.clear();
		x.clear();
		y.clear();
		x.add(x0);
		y.add(y0);
		for(int i=1; i<=3; i++)
		{
			double k1 = h*(derivativeFunction(x0,y0));
			double k2 = h*(derivativeFunction(x0 + (h/2),y0 +(k1/2)));
			double k3 = h*(derivativeFunction(x0+(h/2),y0+(k2/2)));
			double k4 = h*(derivativeFunction(x0+h,y0+k3));
			double yi=y0 +((k1+2*k2 + 2*k3 + k4)/6);
			double xi=x0+i*h;
			x.add(xi);
			y.add(yi);
			
			
		}
		hold.add(x);
		hold.add(y);
		return hold;
	}
	
	public Double derivativeFunction(double x, double y)
	{
		
		
		return Math.pow(y/x, 2)+(y/x);
		
		
	}
	public void adamAlgo()
	{
		double t0=a;
		double w0=IC;
		double h = hmax;
		int flag=1;
		int last =0;
		ArrayList<ArrayList<Double>> first=rungeFourth(h,t0,w0);
		ArrayList<Double> newX= first.get(0);
		ArrayList<Double> newY = first.get(1);
		int nflag=1;
		int i=4;
		double t = newX.get(i-1);
		
		while(flag==1)
		{
			
			double WP = newY.get(i-1) +(h/24)*(55*derivativeFunction(newX.get(i-1),newY.get(i-1))
					-59*derivativeFunction(newX.get(i-2),newY.get(i-2))
					+37*derivativeFunction(newX.get(i-3),newY.get(i-3))
					-9*derivativeFunction(newX.get(i-4),newY.get(i-4)));
			System.out.println("WP "+ WP);
			double WC =newY.get(i-1) +(h/24)*(9*derivativeFunction(t,WP)
					+19*derivativeFunction(newX.get(i-1),newY.get(i-1))
					-5*derivativeFunction(newX.get(i-2),newY.get(i-2))
					+1*derivativeFunction(newX.get(i-3),newY.get(i-3)));
			System.out.println("WC "+ WC);
			double sigma =(19*Math.abs(WC-WP))/(270*h);
			System.out.println(sigma);
			
			if(sigma<=tol)
			{
				
				
				double wi=WC;
				double ti=t;
				
				if(nflag==1)
				{
					int counter=0;
					finalstr="";
					Iterator<Double> it1 = newX.iterator();
					Iterator<Double> it2 = newY.iterator();
					
					while(it1.hasNext())
					{	double point1 = it2.next();
						finalstr = finalstr + "Step " + counter + ":" + " x:" + it1.next() + " y:" + " " + point1 + "\n" ;
						counter++;
					}
					System.out.println(finalstr);
					
					
				}
				else
				{
					
					System.out.println("x: " + ti + "y: " + wi);
					
				}
				
				
				
			}
			if(nflag==1)
			{
				
				flag=0;
				
			}
			else{
				i=i+1;
				nflag=0;
				if(sigma<=0 || newX.get(i-1)+h>b)
				{
					
					 q=Math.pow((tol)/(2*sigma), .25);
					if(q>4)
					{
						h=4*h;
					}
					else
					{
						
						h=q*h;
					}
				
					if(h>hmax)
					{
						h=hmax;
					}
					if(newX.get(i-1) +4*h >b)
					{
						h=(b-newX.get(i-1))/4;
						last=1;
						
					}
					first.clear();
					first=rungeFourth(h,newX.get(i-1),newY.get(i-1));
					newX.clear();
					newY.clear();
					newX=first.get(0);
					newY=first.get(1);
					nflag=1;
					i=i+3;
				
				
				
				}
				q=Math.pow((tol)/(2*sigma), .25);
				
			
			if(q<.1)
			{
				h=.1*h;
				
			}
			else
			{
				
				h=q*h;
				
			}
					
			if(h<hmin)
			{
				
				
				System.out.println("bad");
				
			}
			else
			{
				
				if(nflag==1)
				{
					i=i-3;
				}
				first.clear();
				first=rungeFourth(h,newX.get(i-1),newY.get(i-1));
				newX.clear();
				newY.clear();
				newX=first.get(0);
				newY=first.get(1);
				i=i+3;
				nflag=1;
				
			}
			
			}
			
			
			
			
			
		}
		
		
		
	}
	
	public static void main(String[] args)
	{
		
		AdamVariable one = new AdamVariable();
		one.adamAlgo();
		
		
	}
	
}
