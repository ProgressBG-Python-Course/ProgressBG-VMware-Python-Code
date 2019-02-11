print(f'Number object properties:\n {dir(2)}')
print(f'\nString object properties:\n {dir("test")}')
print(f'\nList object properties:\n {dir([1,2,3])}')
print(f'\nDict object properties:\n {dir({"a":1})}')
print(f'\nFunction (lambda) object properties:\n {dir(lambda x:x**2)}')

def foo(x):
  return x**2

print(f'\nFunction  object properties:\n {dir(foo)}')

