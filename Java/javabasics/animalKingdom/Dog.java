package animalKingdom;

public class Dog extends Animal {

	public Dog(int numLegs, String kingdomName, String genusName, String animalClassName, String soundMade,
			String animalEyeColor, String animalName) {
		super(numLegs, kingdomName, genusName, animalClassName, soundMade, animalEyeColor, animalName);
	}
	
	public void fetch(String item) {
		System.out.println(this.Name + " fetches " + item);
	}

}
