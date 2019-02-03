def foo(**kwargs):
  print(sum(kwargs.values()))



# dict = {
#   'a':3,
#   'b':2,
#   'c':1,
# }
foo(c=1, b=2, a=3) # 6
foo(c=1, b=2) #3