class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


class Developer(Person):
    def __init__(self, name, age, skills):
      # Person.__init__(self, name, age)
      super().__init__(name, age)
      self.skills = skills

class Manager(Person):
  def __init__(self, name, age, managed):
    Person.__init__(self,name, age)
    self.managed = managed

  def __str__(self):
    names = ''
    for dev in self.managed:
      names += f'{dev.name} '

    return names



dev1 = Developer('Pesho', 23, ["Python", "C"])
dev2 = Developer('Maria', 29, ["HTML", "CSS", "JS"])

manager1 = Manager('George', 40, [dev1,dev2])

print(manager1)
# Pesho, Maria