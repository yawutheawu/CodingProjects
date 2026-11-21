package Parking;

public class World {
	public static void main(String args[]) {
		Car x = new Car("Black","4HZG97", "BMW", "M240i Comp");
		x.alertAhead();
		Garage test = new Garage();
		Garage test2 = new Garage(10);
		Garage y = new Garage("General Nathans Mermorial Garage",6);
		System.out.println(x);
		System.out.println(y.getName());
		y.printSpots();
		System.out.println();
		y.parkCar(x,2);
		y.parkCar(x,3);
		y.parkCar(x,4);
		y.parkCar(x,5);
		y.printSpots();
		y.unparkCar(5);
		System.out.println();
		y.printSpots();
		
		int[] search = {40,46,60,300,2000,5000,7077,8000,8001,10000};
		int targetVal = 7077;
		System.out.println(Garage.binarySearch(search,targetVal,0));		

	}
	
}