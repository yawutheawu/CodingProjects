package loops;

public class Arrays {
	public static void main(String[] args) {
		
		//int[] x = new int[5];
		int[] x = {1,2,3,4,5};
		
		for (int i = 0; i< x.length; i++) {
			x[i]= 10;
			System.out.println(x[i]);
		}
		System.out.println();
		
		for (int i : x) {
			i = 10;
			System.out.println(i);
		}
		
		for (int i : x) {
			System.out.println(i);
		}
		
		
		
		
	}
}
