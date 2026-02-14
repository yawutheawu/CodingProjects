import random as r

class Animal:
    def __init__(self, name, age, weight,size,breed, colors):
        self.name = name
        self.age = age
        if type(colors) is list:
            self.colors = colors
        else:
            self.colors = list(colors)
        self.weight = weight
        self.size = size
        self.breed = breed
    
    def eat(self):
        return f"{self.name} is eating."
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
    def smell(self):
        return f"{self.name} is smelling around."
    
    def makeSound(self):
        return f"{self.name} makes a generic sound."


class Dog(Animal):
    def makeSound(self):
        return f"{self.name} says Woof!"
    
    def fetch(self, item):
        # 5 + (r.random() * 75)
        return f"{self.name} runs {round(r.uniform(5, 75),2)} feset to fetch the {item}!"




JohnTheDog = Dog("John", 3, 45, "Medium", "Beagle", ["Brown", "White"])
print(JohnTheDog.makeSound())
print(JohnTheDog.smell())
print(JohnTheDog.fetch("ball"))