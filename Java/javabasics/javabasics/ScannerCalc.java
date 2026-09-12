package javabasics;
import java.util.Scanner;

/*
 * what operation (+,-,*,/)?
 * First number? 
 * Second Number? 
 * Result: 
 */

public class ScannerCalc {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		
		System.out.print("What operation (+,-,*,/,^)? ");
		String operat = console.nextLine();
		System.out.print("First number? ");
		double a = console.nextDouble();
		System.out.print("Second Number? ");
		double b = console.nextDouble();
		
		if (operat.equals("-")) {
			System.out.println("%.2f %s %.2f = %.2f".formatted(a,operat,b,a-b));
		} else if (operat.equals("+")) {
			System.out.println("%.2f %s %.2f = %.2f".formatted(a,operat,b,a+b));
		} else if (operat.equals("*")) {
			System.out.println("%.2f %s %.2f = %.2f".formatted(a,operat,b,a*b));
		} else if (operat.equals("/")) {
			System.out.println("%.2f %s %.2f = %.2f".formatted(a,operat,b,a/b));
		} else if (operat.equals("^")) {
			System.out.println("%.2f %s %.2f = %.2f".formatted(a,operat,b,Math.pow(a,b)));
		}  else {
			System.out.println("Bad Input!");
		}
		
		console.close();
	}
}
