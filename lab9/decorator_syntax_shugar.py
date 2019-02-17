def stars_decorator(f):
  def wrapper():
    print('~'*20)
    f()
    print('~'*20)

  return wrapper

# create decorated functions:
@stars_decorator
def foo():
  print('foo')

foo()
