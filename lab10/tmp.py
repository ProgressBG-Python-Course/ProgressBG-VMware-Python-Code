class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'My name is {self.name}. {self.age} years old.')



class Employee(Person):
    def _init__(self, name, age, cv):
        super().__init__(name, age)
        self.cv = cv


pesho = Employee("Pesho", 32, "CV")

# if pesho is a Person, then execute pesho.gree()
 

if issubclass(type(pesho), Person):
    pesho.greet()


