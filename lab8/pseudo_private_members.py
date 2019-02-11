class A:
  def __init__(self):
    self.public = 'Public'
    self._protected = 'Protected'
    self.__private = 'Private'

  def __str__(self):
    return f'public={self.public}, _protected={self._protected}, __private={self.__private}'

  def get_members(self):
    return self.__dict__


a = A()
print(a.get_members())

a.public = '###'
a._protected = '###'
a.__private = '###'
print(a.get_members())
print(a)