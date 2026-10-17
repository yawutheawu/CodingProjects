package loops;

public class whileLoop {
	public static void main(String[] args) {

		for (int i = 11; i >= 1; i--) {
			for (int n = 0; n < i; n++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		
	}
}