package Parking;

public class Motorbike extends roadMachine {

	public Motorbike(String color, String licensePlateNum, String make, String model, int wheels) {
		super(color, licensePlateNum, make, model, wheels);
	}
	
	@Override
	public void alertAhead() {
		System.out.println(this.Make + " " +  this.Model + " Revs Engine Loudly");
	}

}
