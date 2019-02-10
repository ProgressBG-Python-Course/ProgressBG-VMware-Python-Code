class Person():
  count = 0

  @classmethod
  def increment_counter(cls):
    cls.count += 1
    print("count:",cls.count )

  def __init__(self, name, age):
    self.name = name
    self.age = age

    self.increment_counter()
    # attach count to an object
    self.count = Person.count


  def __str__(self):
    return "{}. {}: {}".format(self.count, self.name, self.age)


maria = Person("Maria", 20)
pesho = Person("Pesho", 30)

print(maria)
print(pesho)

# obviously, we would not want that. So, be careful with class methods!
maria.increment_counter()
pesho.increment_counter()

print(Person.count)