"""
Notes:

  Lexicographical Comparison:
    First the first two items are compared, and if they differ this determines the outcome of the comparison.If they are equal, the next two items are compared, and so on, until either sequence is exhausted

  Comparison operator Chaining:
    https://docs.python.org/3/reference/expressions.html#comparisons
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('"9" > "10000" = {}'.format("9" > "10000") )
# what Python is doing is like:
# print(ord("9") > ord("1"))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('"12" > "1000" = {}'.format("12" > "1000"))
# what Python is doing is like:
# print(ord("2") > ord("0")),
# as the first symbols are the same


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('1<5<10 = {}'.format(1<5<10))
# equivalent to: 1<5 and 5<10

print('1<5>10 = {}'.format(1<5>10))
# equivalent to: 1<5 and 5>10

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 4
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# next will throw  a TypeError, as Python3
# will not compare "oranges" with "apples"
# Python2 will be ok with that
print('"3" > 2 = {}'.format("3" > 2))