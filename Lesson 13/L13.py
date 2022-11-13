from math import sqrt
import datetime
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return f'({self.x},{self.y})'
    def __mul__(self,num):
        return Point(self.x*num,self.y*num)
    __rmul__=__mul__
    def __abs__(self):
        return sqrt(self.x**2+self.y**2)
    def __gt__(self,other):
        return abs(self)>abs(other)
    def __add__(self):
        return self.x+self.y  
    __radd__=__add__
    def __eq__(self,other):
        return (type(self.x) == type(other))
       
## Main Program ##
p1=Point([-2+4,-12+45])
p3 = Point(12,0.3345)
p2 = Point(12,45)
p2=3*p1
print(type(p1[:]))
print(p2)
print(p1 == p3)
a = [5,5]
b = [15,]
print(type(a) == type(b))
print(type(p1))
# p2<p1 --> p2.__lt__(p1) --> builtins.object --> NotImplemented
# p1.__gt__(p2)
print(type(p3))

