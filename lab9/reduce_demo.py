from functools import reduce


# how reduce work (a rough exampple):
def fake_reduce(f,l):
	l = list(l)

	for i, _ in enumerate(l):
		if i == 0:
			continue
		elif i == 1:
			x = l[0]
			y = l[1]		
		else:
			x = res
			y = l[i]

		res = f(x,y)
		print(f"\ti = {i}, res = {res}")

	return res


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# demo1 - done TODO in labs
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
l = [2, 2, 0, 2]

reduced_l = reduce( lambda x,y: x/y, filter(lambda x:x, l))
print( f"reduced_l: {reduced_l}\n" )

faked_reduced_l =  fake_reduce(lambda x,y: x/y, filter(lambda x:x, l))
print(f"faked_reduced_l: {faked_reduced_l}\n")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# demo2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# calculates ((((1+2)+3)+4)+5
l = [1, 2, 3, 4, 5]

reduced_l = reduce(lambda x, y: x+y, l) 
print( f"reduced_l: {reduced_l}" )

faked_reduced_l =  fake_reduce(lambda x, y: x+y, l)
print(f"faked_reduced_l: {faked_reduced_l}")


