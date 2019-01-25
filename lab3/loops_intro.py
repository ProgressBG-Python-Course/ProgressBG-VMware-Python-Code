"""Notes

  We use 'while' loops when we don't know
  how many iterations we need

  If we know the exact number of iterations,
  we use the 'for' loop
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sum = 0
for num in [1,2,3]:
  sum += num

print(f'The sum of 1,2,3 is: {sum}\n')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user_pass = input("Enter a pass:")

while len(user_pass)<3:
  user_pass = input("\nYour pass has to be > 3 symbols.\nTry again:")

print(f'Your password is {user_pass}. Bye!')

