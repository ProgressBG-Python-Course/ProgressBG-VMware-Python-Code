def stars_decorator(f):
  f("maria")


  # def wrapper():
  #   print("*" * 50)
  #   f()
  #   print("*" * 50)

  # return wrapper


def greet(user):
  print(f"Howdy {user}!")

# let's decorate greet:
stars_decorator(greet)
greet("Maria")

# and use it:
# greet("maria")