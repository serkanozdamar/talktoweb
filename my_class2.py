class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, f, l, class_info):
        super().__init__(f, l)
        self.class_info = class_info

    def printname(self):
        super().printname()
        print(self.firstname, self.lastname, self.class_info)


p = Person("Mike", "Olsen")
x = Student("Mike 2", "Olsen 2", "10-B")

p.printname()
x.printname()
