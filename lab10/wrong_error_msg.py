class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)
 
class Employee(Person):
  """docstring for Employee"""
def __init__(self, name, age, skills):
    Person.__init__(self, name, age)
    self.skills = skills
 
def __str__(self):
    # return super().__str__() + ". Has salary: {}".format(self.salary)
    return Person.__str__(self) + ". Has skills: {}".format(self.skills)
 
def numberofskills(self):
    print(len(self.skills))

pesho = Employee("Pesho", 25, ["Python", "JS"])
maria = Employee("maria", 20, ["Java", "Rubi"])
 

print(pesho.numberofskills())
print(pesho)
print(maria)


print("pesho + maria = ",pesho + maria)

# pesho + maria =  6000