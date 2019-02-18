from functools import reduce

l = [2, 2, 0, 2]

# TODO: check return value....
l2 = reduce( lambda x,y: x/y, filter(lambda x:x, l))




print( l2 )

# educe(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5

