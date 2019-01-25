"""
Notes:
  x and y =  x if x is False, else y
  (False and whatever is always False.)

  x or y =  x if x is True, else y
  (True or whatever is always True.)

  'and' and 'or' returns one of their operands
  'not' always returns boolean value

  'and' is with higher precedence than 'or'
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('~'*10, 'example 1','~'*10)
a = 1 or 0
b = 1 and 0
print(f'a={a}')
print(f'b={b}')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('~'*10, 'example 2','~'*10)
wine = "Mavrud"
beer = "Grolsch"
whiskey = ""
# note the brackets that change the precedence
print('Drink', whiskey and beer or wine)
print('Drink', whiskey and (beer or wine))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('~'*10, 'example 3','~'*10)
to_be = 'Just be'
print(to_be or not to_be)
print(to_be and not to_be)
