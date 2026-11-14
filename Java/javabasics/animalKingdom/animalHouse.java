package animalKingdom;

public class animalHouse {
	public static void main(String args[]) {
		Cat sirMeowster = new Cat(4, "Animalia", "Felis", "Mammalia", "Meow", "Yellow", "Sir Meowster");
		Dog frank = new Dog(4, "Animalia", "Canis", "Mammalia", "Bark", "Green", "Franklin");
		
		sirMeowster.makeSound();
		frank.makeSound();
		sirMeowster.attackOwnerForNoReason();
		frank.fetch("Frank's Favorite Ball");
		
	}

}
