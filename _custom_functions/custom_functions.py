def preaty_print(msg, obj):
	delim = '~'
	delim_count = 70

	print(delim*delim_count)

	print(msg, end='\n\t')
	if type(obj) in (list,tuple):
		print(*obj, end='\n', sep='\n\t')
	else:
		print(obj, end='\n', sep='\n\t')

	print(delim*delim_count, '\n')