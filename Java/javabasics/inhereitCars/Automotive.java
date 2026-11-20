package inhereitCars;

public class Automotive {
	
	/*
	 * - Make 
		- Model
		- Color
		- Trim
		- Number of Wheels
		- Number of Seat
		- License plate
		- Engine Model
	 */
	
	protected String Make;
	protected String Model;
	protected String Color;
	protected String Trim;
	protected int NumWheels;
	protected double NumSeats;
	protected String LicensePlate;
	protected String EngineModel;
	
	// Default Constructor
	public Automotive() {
		this("Default Make", "Default Model", "Black", "Unregistered");
	}
	
	//Shortened Const.
	public Automotive(String VecMake, String VecModel, String VecColor, String VecLicensePlate) {
		this.Make = VecMake;
		this.Model = VecModel;
		this.Color = VecColor;
		this.LicensePlate = VecLicensePlate;
		this.Trim = "Base";
		this.NumWheels = 4;
		this.NumSeats = 4.5;
	}
	
	//Full Const.
	public Automotive(String VecMake, 
					  String VecModel, 
					  String VecColor, 
					  String VecTrim, 
					  int VecWheels,
					  double VecSeats,
					  String VecLicensePlate,
					  String VecEngineModel) {
		this.Make = VecMake;
		this.Model = VecModel;
		this.Color = VecColor;
		this.Trim = VecTrim;
		this.NumWheels = VecWheels;
		this.NumSeats = VecSeats;
		this.LicensePlate = VecLicensePlate;
		this.EngineModel = VecEngineModel;
	}
}
