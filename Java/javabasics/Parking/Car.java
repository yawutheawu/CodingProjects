package Parking;

public class Car {
	
	private String Color;
	private String LicensePlate;
	private String Make;
	private String Model;
	private boolean Parked;
	
	public Car(String color, String licensePlateNum, String make, String model) {
		this.Color = color;
		this.LicensePlate = licensePlateNum;
		this.Make = make;
		this.Model = model;
		this.Parked = false;
	}
	
	public String getColor() {
		return this.Color;
	}
	
	public void setColor(String newCol) {
		this.Color = newCol;
	}
	
	public String getPlate() {
		return this.LicensePlate;
	}
	
	public void setPlate(String newPlate) {
		this.Color = newPlate;
	}
	
	public String getMake() {
		return this.Make;
	}
	
	public void setMake(String newMake) {
		this.Color = newMake;
	}
	
	public String getModel() {
		return this.Model;
	}
	
	public void setModel(String newModel) {
		this.Color = newModel;
	}
	
	public void setParked(boolean newPark) {
		this.Parked = newPark;
	}
	
	

}
