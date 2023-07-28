class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old")


class Cat(Pet):
    # If we have another parameter for color in cat
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print('Bark')


pet = Pet('Natu', 25)
pet.show()

cat = Cat('Uru', 22, 'Brown')
cat.show()
cat.speak()

dog = Dog('Bagira', 1)
dog.show()
dog.speak()
