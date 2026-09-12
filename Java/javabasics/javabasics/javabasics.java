package javabasics;

public class javabasics {
	public static void main(String[] args) {
//		String x = "Hello World";
//		System.out.println(x);
//		int y  = 10;
//		System.out.println(y);
//		boolean z = true;
//		System.out.println(z);
//		double n = 10.75;
//		System.out.println(n);
//		char u = 'i';
//		System.out.println(u);

		// and -> &&
		// or -> ||
		// not -> !

//		if (false) {
//			System.out.println("Hello");
//		} else if (true) {
//			System.out.println("Bye");
//		} else {
//			System.out.println("No");
//		}

		String oper = "+";
		int a = 10;
		int b = 5;
		if (oper.equals("+")) {
			System.out.println(a + b);
		} else if (oper.equals("-")) {
			System.out.println(a - b);
		} else {
			System.out.println("Bad Input");
		}

	}
}
