# functions are first-class objects
if 1:
  def add(x,y):
    print(x+y)

  print(type(add))

  # so we can attach properties to functions
  add.id = 1
  print(add.id)





# bind a function object to more than 1 names
if 0:
  def foo():
    print('foo()')

  bar = foo

  foo()
  bar()

