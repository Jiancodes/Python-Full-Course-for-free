class Animal:

    def eat(self):
        print("Tis animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("The rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()