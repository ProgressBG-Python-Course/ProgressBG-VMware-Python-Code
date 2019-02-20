# With one argument, type() return the type of an object.
print( type("a string") )

# the same as above
print( "aa string".__class__)

# classes in python are objects, as well, so:
print( type(str) )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# type for dynamic class creation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Employee = type('Employee', (object,), dict())

class Employee2:
    pass

pesho = Employee()
print(dir(pesho))

print( hasattr(pesho, '__dict__'))

