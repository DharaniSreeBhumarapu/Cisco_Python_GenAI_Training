class Animal:
    def speak(self):
        print("Animal makes Sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak() # invoke parent class - To avoid methodoverriding
obj1 = Dog()
obj1.speak()
