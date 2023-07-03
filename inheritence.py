class Animal:
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age

    def speak(self):
        raise NotImplementedError("Child classes must implement this")


class Dog(Animal):
    def speak(self):
        return "Barks"

class Cat(Animal):
    def speak(self):
        return "Meows"


class Lion(Animal):
    def speak(self):
        return "Roars"


dog = Dog("Bosco", "Black and white", "3 years")
print(dog.name)
print(dog.speak())
print(dog.colour)

cat = Cat("Sucrose", "Grey", "2 years")
print(cat.name)
print(cat.speak())
print(cat.colour)

lion = Lion("The wild lion", "Golden Brown", "3 years")
print(lion.name)
print(lion.speak())
print(lion.colour)