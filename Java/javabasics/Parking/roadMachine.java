package Parking;

public class roadMachine {
	
	protected String Color;
	protected String LicensePlate;
	protected String Make;
	protected String Model;
	protected int Wheels;
	protected boolean Parked;
	
	public roadMachine(String color, String licensePlateNum, String make, String model,int wheels) {
		this.Color = color;
		this.LicensePlate = licensePlateNum;
		this.Make = make;
		this.Model = model;
		this.Wheels = wheels;
		this.Parked = false;
	}
	
	public int getWheels() {
		return this.Wheels;
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
	
	public void alertAhead() {
		System.out.println(this.Make + " " +  this.Model + " honks");
	}
	
}
