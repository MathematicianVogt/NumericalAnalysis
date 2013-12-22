import java.util.Scanner;


public class romberg {
public static Double[][] rom;
static double first;
static double second;
static double n;
static double sum;
static double h;
static double r11;
static double tol;
public static double function(double x)
{
	return 1/(Math.log(x)*x);
	//return Math.pow(Math.sin(x), 2) -2*x*Math.sin(x) +1;
	//return x*Math.log(x+1);
	//return Math.pow(Math.cos(x), 2);
}	
public static void colmb(int k, int colnum)
{	double exponent=colnum+1;
	for (int t=k; t<=n; t++)
	{
		
		rom[t][colnum]=rom[t][colnum-1] + (1/((Math.pow(4, exponent-1))-1))*(rom[t][colnum-1] - rom[t-1][colnum-1]);
		exponent++;
		
	}
	
}
public static void tolerenceMet()
{
	
for(int i=1; i<n; i++)
{
	System.out.println("Differences between are " + Math.abs((rom[i][i-1]-rom[i+1][i])) );

	
	
	if(Math.abs(rom[i][i-1]-rom[i+1][i])<tol)
	{
		
		System.out.println("Converge to " + rom[i][i-1] +" at n equals " + i);
		break;
	}
	
	
}



}
public static void print()
{
	
	for(int i = 0; i < rom.length; i++)
	{
	    for(int j = 0; j < rom[i].length; j++)
	    {
	        System.out.print(rom[i][j]);
	        if(j < rom[i].length - 1) System.out.print(" ");
	    }
	    System.out.println();
	}
	
}
public static void AllOtherCols()
{
	
	for(int i=2; i<=n; i++)
	{
		
		colmb(i,i-1);
	}
	
}
public static void firstCols()
{
	
	for (int i=2; i<=n; i++)
	{
		
		
		for(int j=1; j<=Math.pow(2, i-2); j++)
		{
			
			sum=sum+function(first+((2*j -1)*((second-first)/(Math.pow(2, i-1)))));
		}
		
		rom[i][0]=.5*(rom[i-1][0] +((second-first)/(Math.pow(2, i-2)))*sum);
		sum=0;
		
		
	}
	
}
public static void define()
{
	Scanner in = new Scanner(System.in);
	rom = new Double[11][11];
	first=Math.E;
	second=2*Math.E;
	tol=in.nextDouble();
	n =10;
	sum=0;
	h=second-first;
	r11=(h/2)*(function(first)+function(second));
	rom[1][0]=r11;
	
}

public static void main(String[] args)
{	define();
	firstCols();
	AllOtherCols();
	print();
	tolerenceMet();

}
	
}
