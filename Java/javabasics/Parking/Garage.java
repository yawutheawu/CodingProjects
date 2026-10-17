package Parking;

public class Garage {
	/*
	 * Size of Garage
	 * Name of Garage
	 */

	private String garageName;
	private int garageSize;
	private Car[] spots;

	public Garage(String Name, int Size) {
		this.garageName = Name;
		this.garageSize = Size;
		this.spots = new Car[Size];
	}

	//Temp or Dev function
	public void printSpots() {
		for (Car i : spots) {
			if (i != null) {
				System.out.println(i.getMake() + i.getModel());

			} else {
				System.out.println("Empty");

			}
		}
	}
	
	public boolean parkCar(Car carToPark, int spaceIndex) {
		if (this.spots[spaceIndex] == null) {
			this.spots[spaceIndex] = carToPark;
			return true;
		} else {
			return false;
		}
		
	}
	
	public boolean unparkCar(int spaceIndex) {
		if (this.spots[spaceIndex] == null) {
			return false;
		} else {
			this.spots[spaceIndex] = null;
			return true;
		}
	}

	public int getSize() {
		return this.garageSize;
	}

	public void setSize(int newSize) {
		this.garageSize = newSize;
	}

	public void setName(String newName) {
		this.garageName = newName;
	}

	public String getName() {
		return this.garageName;
	}

}
