# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# fruits prices presented as list:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 'apples', 'oranges', 'bananas'
prices_list = [2.50, 2.43, 3.50];



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# fruits prices presented as dictionary:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prices_dict = {
	'apples': 2.50, 
	'oranges': 2.433745438,  # 2.4
	'bananas': 3.50787843,
	'strawberry': 3.4		
}

# get value by key:
print('\nget value by key')
print( prices_dict['oranges'])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# loop on dictionary keys
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('\nloop on dictionary keys:')

for key in prices_dict:
	print( '{} - {:.2f}'.format(key, prices_dict[key]) )

# this is equivalent to above:
# for k,v in prices_dict.keys():
# 	print( '{} - {:.2f}'.format(key, value) )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# loop on dictionary values
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('\nloop on dictionary values:')
for value in prices_dict.values():
	# no way to get the corresponding key	
	print( '{:.2f}'.format(value) )	


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# loop on dictionary key,value pairs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('\nloop on dictionary key,value pairs')
for k,v in prices_dict.items():
	print( '{} - {:.2f}'.format(k,v) )


# note that prices_dict.items() returns a (key,value) tuple. So, if we define only one variable in for, we'll get the whole tuple, not the respective key, value. I.e.:
print('\nloop on dictionary (key,value) pairs as tuple')
for t in prices_dict.items():
	print(t)
	# but we can still access the key,value inside the tuple:
	# print( '{} - {:.2f}'.format(t[0], t[1]) )
