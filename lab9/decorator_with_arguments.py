# decorator with arguments should return a function that will take a function
# and return another function.
def sign_decorator(sign):
  def decorator_wrapper(f):
    def decorator():
      print(sign*20)
      f()
      print(sign*20)
    return decorator
  return decorator_wrapper

# create decorated functions:
@sign_decorator('*')
def foo():
  print('foo')

@sign_decorator('~')
def bar():
  print('bar')

foo()
bar()
