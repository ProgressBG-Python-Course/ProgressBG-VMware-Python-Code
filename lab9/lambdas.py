
def foo(f,a,b):
  print( f(a,b) )

# def my_add(x,y):
#   return x+y

foo( lambda x,y: x+y, 2,3 )

bar = lambda x,y: x+y
# 5

