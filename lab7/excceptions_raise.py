try:
  w = float(input('weight:'))
  print(w)
except ValueError:
  print('\n*** log the ValueError ***\n');
  raise
else:
  print('Nice try')


print('Program End')

