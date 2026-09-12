package javabasics;

import java.util.Scanner;

public class NewScannerCalc {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		System.out.print("Which operation do you want to do? (+,-,*,/, ^) ");
		String op = console.next();
		System.out.print("First Number? ");
		double a = console.nextDouble();
		System.out.print("Second Number? ");
		double b = console.nextDouble();
		System.out.println("%.2f %s %.2f = %.2f".formatted(a,op,b,calculate(a,b,op)));
		
		console.close();
		
		}
	
	public static double calculate(double a, double b, String operat) {
		double ans;
		if (operat.equals("+")) {
			ans = a + b;
		} else if (operat.equals("-")) {
			ans = a - b;
		} else if (operat.equals("*")) {
			ans = a * b;
		} else if (operat.equals("/")) {
			ans = a / b;
		} else if (operat.equals("^")) {
			ans = Math.pow(a, b);
		} else {
			System.out.println("Bad Input!");
			ans = 0.0;
			
		}
		return ans;
	}
}
