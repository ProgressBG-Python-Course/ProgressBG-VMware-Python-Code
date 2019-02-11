# add_num() definition
def add_num(*args):
  # res = 0
  # for item in args:
  #   res += item

  print(sum(args))


# test your code:
add_num(1)
#should print 1

add_num(1,2)
#should print 3

add_num(1,2,3)
#should print 6