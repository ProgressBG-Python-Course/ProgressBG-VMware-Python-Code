x = 2

def outer():
  x = 3

  def inner():
    nonlocal x
    x = x + 2
    print(f'1: x = {x}')

  inner()

outer()
print(f'2: x = {x}')

# 1.5
# 2.2
