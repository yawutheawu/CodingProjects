package animalKingdom;

public class Cat extends Animal {
	public Cat(int numLegs, String kingdomName, String genusName, String animalClassName, String soundMade,
			String animalEyeColor, String animalName) {
		super(numLegs, kingdomName, genusName, animalClassName, soundMade, animalEyeColor, animalName);
	}
	
	public void attackOwnerForNoReason() {
		System.out.println(this.Name + " thinks your ankles look like good prey and pounces");
	}
}
