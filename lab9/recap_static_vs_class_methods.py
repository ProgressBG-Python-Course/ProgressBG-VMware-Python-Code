class A:
  """
    Static methods do not take object/class reference as first parameter.
    Class methos take class reference as their first parameter
    Normal methods take object reference ad their first parameter
  """

  @staticmethod
  def static_method(x):
    print(f'{x} from static method in A')

  @classmethod
  def class_method(self,x):
    print(f'{x} from class method in {self}')

# B inherits A
class B(A):
  pass


a = A()
b = B()


# static method does not cares who calls it
a.static_method(2)
b.static_method(2)
A.static_method(2)
B.static_method(2)

# class method knows that it's called from the specific class
a.class_method(2)
b.class_method(2)
A.class_method(2)
B.class_method(2)
