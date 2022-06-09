class Animal:
    species = "animal"

    def __init__(self, age, name, colour, breed, gender, kind):
        self.age = age
        self.name = name
        self.colour = colour
        self.breed = breed
        self.gender = gender
        self.kind = kind
    def intro(self):
        print("{} is an animal of {} kingdom".format(self.name, self.species))
        print("{} is {}  years old.  {} breed is {}. {} colour is {}. {} gender is {}. {} is a {}.".format(self.name, self.age, self.name, self.breed, self.name, self.colour, self.name, self.gender, self.name, self.kind))




class Dog(Animal):
     def __init__(self, Animal):
         super(Animal, self).__init__(Animal)
begal = Animal(12, "begal", "green", "russian", "male","Dog")
bela = Animal(10, "bela", "red", "chinies", "female", "Dog")
spike = Animal(15, "spike", "white", "bully", "male", "DOg")

puppy1 = begal
puppy2 = bela
puppy3 = spike

# puppy1.intro()
# puppy2.intro()
# puppy3.intro()


class Cat(Animal):
    def __init__(self, Animal):
        super(Animal, self).__init__(Animal)


snow_bell = Animal(5, "snow_bell", "white", "persian", "female", "cat")
jerry = Animal(4, "jerry", "black", "himalyian", "male", "cat")
tom = Animal(6, "tom", "brown", "egyption", "male", "cat")

cat1 = snow_bell
cat2 = jerry
cat3 = tom

cat1.intro()
cat2.intro()
cat3.intro()

puppy1.intro()
puppy2.intro()
puppy3.intro()