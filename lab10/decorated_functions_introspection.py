import time
from functools import reduce

def timeit(f):
    def wrapper(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print("Function '{}' took {:f} ms".format(f.__name__, te -ts))

        return result
    return wrapper

@timeit
def sum1(min, max):
    return reduce(lambda x,y: x+y, range(min,max+1))

@timeit
def sum2(min, max):
    return sum(range(min,max+1))

print( sum1(1,1_000_000) )
print( sum2(1,1_000_000) )