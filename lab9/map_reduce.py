def map_iterable():
  l1 = [1,2,3]

  mapped = map(lambda el:el*2, l1)
  print(mapped)
  print(list(mapped))


def map_iterables():
  l1 = [1,2,3]
  l2 = [1,2,3]
  l3 = [1,2,3]


  print(list(map(lambda a,b,c: a+b+c, l1,l2,l3)))


def map_reduce_iterables_demo():
  from functools import reduce

  l1 = [1,2,3]
  l2 = [1,2,3]
  l3 = [1,2,3]

  l = map(lambda * t: reduce(lambda a,b: a+b, t) , l1, l2,l3)
  print( list(l) )


map_reduce_iterables_demo()