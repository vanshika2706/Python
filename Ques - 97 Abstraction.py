from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the speak method
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
