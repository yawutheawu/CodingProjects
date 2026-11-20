package inhereitCars;

public class Car extends Automotive {

	public Car() {
		super();
	}

	public Car(String VecMake, String VecModel, String VecColor, String VecLicensePlate) {
		super(VecMake, VecModel, VecColor, VecLicensePlate);
	}

	public Car(String VecMake, String VecModel, String VecColor, String VecTrim, int VecWheels, double VecSeats,
			String VecLicensePlate, String VecEngineModel) {
		super(VecMake, VecModel, VecColor, VecTrim, VecWheels, VecSeats, VecLicensePlate, VecEngineModel);
	}

}
