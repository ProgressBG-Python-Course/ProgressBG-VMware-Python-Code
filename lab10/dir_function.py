number = 2
string = 'this is a string' 

print('list of names in the current local scope:')
print( dir() )

print('\nlist of valid attributes for an object:')
print( dir(number) )
print( dir(string) )

class Point():    
    def __init__(self,x,y):        
        self.x = x 
        self.y = y

    def foo(self):
        print('foo')

a = Point(2,3)
print('custom object')
print( dir(a) )
print( dir(Point) )



