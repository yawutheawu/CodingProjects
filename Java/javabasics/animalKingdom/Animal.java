package animalKingdom;

public class Animal {
	protected int legs;
	protected String kingdom;
	protected String genus;
	protected String animalClass;
	protected String sound;
	protected String eyecolor;
	protected String Name;
	
	
	public Animal(int numLegs, 
				  String kingdomName,
				  String genusName,
				  String animalClassName,
				  String soundMade,
				  String animalEyeColor,
				  String animalName) {
		this.legs = numLegs;
		this.kingdom = kingdomName;
		this.genus = genusName;
		this.animalClass = animalClassName;
		this.sound = soundMade;
		this.eyecolor = animalEyeColor;
		this.Name = animalName;
	}
	
	public void setLegs(int newLegs) {
		this.legs = newLegs;
	}
	public int getLegs() {
		return this.legs;
	}
	
	public void setKingdom(String newKingdom) {
		this.kingdom = newKingdom;
	}
	public String Kingdom() {
		return this.kingdom;
	}
	
	public void setGenus(String newGenus) {
		this.genus = newGenus;
	}
	public String getGenus() {
		return this.genus;
	}
	
	public void setClass(String newClass) {
		this.animalClass = newClass;
	}
	public String Class() {
		return this.animalClass;
	}
	
	public void setSound(String newSound) {
		this.sound = newSound;
	}
	public String getSound() {
		return this.sound;
	}
	
	public void setEyecolor(String newEyecolor) {
		this.eyecolor = newEyecolor;
	}
	public String getEyecolor() {
		return this.eyecolor;
	}
	
	public void setName(String newName) {
		this.Name = newName;
	}
	public String getName() {
		return this.Name;
	}
	
	public void makeSound() {
		System.out.println(this.Name + ": " + this.sound);
	}
	
}
