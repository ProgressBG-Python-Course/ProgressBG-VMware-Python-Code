# next two statements do equivalent job:
print('|%10.2f|%10.2f|' % (3.14, 2.5))
print('|{:10.2f}|{:10.2f}|'.format(3.14, 2.5))

# let's center the values
print('|{:^10.2f}|{:^10.2f}|'.format(3.14, 2.5))