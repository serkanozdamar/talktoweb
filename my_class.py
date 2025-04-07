import random

class Person:

    def __init__(self, name:str="No name", age:int=25, *args, **kwargs):
        self.name = name
        self.age = age
        self.power = None
        self.__car__ = "Mercedes"
        if "power" in kwargs:
            self.power = kwargs["power"]

    def attack(self):
        if self.power > 0:
            self.power -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} is {self.age} years old with power {self.power}."

people = []
for i in range(100):
    people.append(Person(f"John-{i}", random.randint(20, 40)))
    # people[-1].attack()

print(people[0].name, people[0].age, people[0].power)
print(people[-1].name, people[-1].age, people[-1].power)

superPerson = Person("5",7,9,7, power=1000, ali="mehmet")
print(superPerson.name)
print(superPerson)

superPerson.address = "Ankara"
print(superPerson.__dict__)
print(superPerson.__car__)

print(people[0].__dict__)
print(people[0].__car__)

my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3


print(my_dict)