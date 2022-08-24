

class Student:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def printname(self):
        return f'Firstname: {self.firstname}\nLastname: {self.lastname}\nAge:{self.age}'


class Teacher(Student):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age)


J = Teacher("Samsom", "Josh", 28)
O = Teacher("Tochukwu", "David", 40)

print(Teacher.printname(J), '\n',Teacher.printname(O))