# common sets use case: get unique values from list:
numbers = [1,1,2,3,4,5,3,2]
print( 'unique numbers:', set(numbers) )


# set operations
a = {1,2,3}
b = {3,4,5,6}

# difference is not commutative operation
print('a - b = ', a.difference(b) )
print('b - a = ', b.difference(a) )