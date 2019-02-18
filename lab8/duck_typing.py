class Duck:
   def quack(self):
      print('Quack, Quack')

class Goose:
  pass
   # def quack(self):
   #    # print('Quack!')
   #    pass


def quack(obj):
   obj.quack()


donald = Duck()
lea = Goose()

quack(donald)
quack(lea)