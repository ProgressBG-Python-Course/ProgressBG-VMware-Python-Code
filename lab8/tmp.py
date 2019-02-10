class A:
  count=0

  @classmethod
  def counter(cls):
    cls.count += 1
    print(cls.count)



A.counter();
