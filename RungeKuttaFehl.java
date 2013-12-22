import java.util.Scanner;


public class RungeKuttaFehl {
public double function(double t, double y)
{
	
	return Math.pow(t, 2);
	//return (Math.pow(y, 2)+y)/t;
	//return Math.sin(t)+Math.exp(-t);
	//return Math.pow(y/t, 2) + (y/t);
	
	
}

public void algo()
{
	Scanner in = new Scanner(System.in);
	System.out.println("a");
	double a = in.nextDouble();
	System.out.println("b");
	double b = in.nextDouble();
	System.out.println("IC");
	double IC = in.nextDouble();
	System.out.println("TOL");
	double tol = in.nextDouble();
	System.out.println("hmax");
	double hmax = in.nextDouble();
	System.out.println("hmin");
	double hmin=in.nextDouble();
	double t=a;
	double w=IC;
	double h = hmax;
	int flag=1;
	double k1;
	double k2;
	double k3;
	double k4;
	double k5;
	double k6;
	double R;
	double delta;
	while(flag==1)
	{
	 k1=h*function(t,w);
	 k2 = h*function(t + (1.0/4.0)*h, w+(1.0/4.0)*k1);
	 k3=h*function(t+(3.0/8.0)*h,w+ (3.0/32.0)*k1 + (9.0/32.0)*k2);
	 k4=h*function(t+(12.0/13.0)*h,w+(1932.0/2197.0)*k1 -(7200.0/2197.0)*k2 +(7296.0/2197.0)*k3);
	 k5=h*function(t+h,w +(439.0/216.0)*k1- 8.0*k2 +(3680.0/513.0)*k3 -(845.0/4104.0)*k4);
	 k6=h*function(t+(.5*h), w-(8.0/27.0)*k1 +2*k2-(3544.0/2565.0)*k3 +(1859.0/4104.0)*k4 -(11.0/40.0)*k5);
	 R=(1/h)*Math.abs((1.0/360.0)*k1 -(128.0/4275.0)*k3 -(2197.0/75240.0)*k4 +(1.0/50.0)*k5 +(2.0/55.0)*k6);
	 if(R<=tol)
	 {
		 
		 t=t+h;
		 w=w+(25/216)*k1 +(1408.0/2565.0)*k3 +(2197.0/4104.0)*k4 - (1.0/5.0)*k5;
		 System.out.println("t:" + t + " w:" + w + " h:" + h);
		 
	 }
	delta=.84*Math.pow(tol/R, .25);
	if (delta<=.1)
	{
		
		h=.1*h;
		
	}
	else if(delta>=4)
	{
		h=4*h;
		
	}
	else{
		
		h=delta*h;
		
	}
	if(h>hmax)
	{
		
		h=hmax;
	}
	
	if(t>=b)
	{
		flag=0;
		
	}
	else if(t+h>b)
	{
		
		h=b-t;
		
	}
	else if(h<hmin){
		flag=0;
		System.out.println("Minimum reached");
		
	}
	
	}
	
}
	
public static void main(String[] args)
{
	RungeKuttaFehl go = new RungeKuttaFehl();
	go.algo();
	
	
}

}
