# super() access to base methods - example
class Absolute():
  def __str__(self):
    return "*********"

class Person(Absolute):
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # def __str__(self):
  #   return "{} is {} years old".format(self.name, self.age)

class Employee(Person):
  """docstring for Employee"""
  def __init__(self, name, age, salary):
    super().__init__(name,age)
    self.salary = salary

  def __str__(self):
    # return super().__str__() + ". Has salary: {}".format(self.salary)
    return super().__str__() + ". Has salary: {}".format(self.salary)

  def print_super(self):
    print( self.__str__(),"\n\n")


pesho = Employee("Pesho",25, 3500)
# print(pesho.__class__)
pesho.print_super();