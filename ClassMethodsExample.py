class Person:
    number_of_person = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_person

    @classmethod
    def add_person(cls):
        cls.number_of_person += 1


person1 = Person('Uru')
person2 = Person('Natu')
print(Person.get_number_of_people())
