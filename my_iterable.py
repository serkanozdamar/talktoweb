class Person:
    def __init__(self, firstname, lastname, tckn):
        self.firstname = firstname
        self.lastname = lastname
        self.tckn = tckn

class Bus:
    def __init__(self, name):
        self.name = name
        self.index = 0
        self.__passengers__ = {
            "01": None,
            "02": None,
            "03": None,
            "04": None,
            "05": None
        }

    def add_passenger(self, seat_no, passenger):
        self.__passengers__[seat_no] = passenger

    def __iter__(self):
        return self.__passengers__
        #return self.__passengers__.items()
        #return self


    def __next__(self):
        if self.index >= len(self.__passengers__) -1:
            raise StopIteration
        x = self.index
        self.index += 1

        my_keys = self.__passengers__.keys()
        my_keys = list(my_keys)
        real_key = my_keys[self.index]
        return self.__passengers__[real_key].firstname



p1 = Person("John", "Doe", 100)
p2 = Person("Ali", "Doe", 100)
p3 = Person("Veli", "Doe", 100)
p4 = Person("Deli", "Doe", 100)
p5 = Person("Jeli", "Doe", 100)

my_bus = Bus("Varan Turizm")
my_bus.add_passenger("01", p1)
my_bus.add_passenger("02", p2)
my_bus.add_passenger("03", p3)
my_bus.add_passenger("04", p4)
my_bus.add_passenger("05", p5)

# sentinel value

for k,v in my_bus.__iter__().items():
    print(k)
