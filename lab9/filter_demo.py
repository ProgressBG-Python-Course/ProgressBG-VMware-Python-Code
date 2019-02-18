l = [1,2,3,4,5,6]


# even_l = []

# for i in l:
#   if i%2==0:
#     even_l.append(i)



# def is_even(i):
#   if i%2==0:
#     return True
#   else:
#     return False


# if cond1:
#   body1
# else:
#   body2

# x = body1 if cond1 else body2

even_numbers = filter(lambda x: x%2==0 if x!=0 else False, range(10))

even_l = filter( lambda i: i%2==0, l)
print( list(even_l) )


