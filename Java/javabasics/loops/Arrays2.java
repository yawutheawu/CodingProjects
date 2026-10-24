package loops;

public class Arrays2 {

	public static void main(String[] args) {
		
		int[] x = {10,20,25,23,50};
		double[] y = new double[10];
		
		//set values of y
		
		for (int i = 0; i < y.length; i++) {
			y[i] = y[i] + 1.0;
			System.out.print(i + " ");
		}
		System.out.println();
		
		
		//print y
		for (int i = 0; i < y.length; i++) {
			System.out.print(y[i] + " ");
		}
		System.out.println();
		for (double i : y) {
			System.out.print(i + " ");
		}

	}

}
