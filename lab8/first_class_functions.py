#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# wherever we call a function it's value is returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add(x,y):
  return x+y

def pow(x,y):
  return  x**y

print(pow(add(2,3),2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a function can be passed as argument
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def foo():
#   print('foo() was called')

# def caller(callback):
#   callback()

# caller(foo)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a function can return another function
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def foo(x):
  def bar(y):
    print('bar was called')
    print(f'x = {x}, y = {y}')

  return bar

baz = foo(2)
baz(3)

# or in one-line with 'currying'
print( foo(2)(3) )


