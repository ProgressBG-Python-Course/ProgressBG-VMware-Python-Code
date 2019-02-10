class Person:
  def __init__(self, name, age):
    self.age = age
    self.name = name
    print(f'self id: {id(self)}')

  def __str__(self):
    return f'name: {self.name}, age:{self.age}'

  def __repr__(self):
    return '''class Person:
    def __init__(self, name, age):
      self.age = age
      self.name = name
      print(f'self id: {id(''self)}')'''


maria = Person('Maria', 23)
print(maria)

# maria.__repr__()
