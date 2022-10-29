from math import sqrt
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    @property
    def mag(self):
        return sqrt(self.x**2+self.y**2)
    def res(self):
        return (self.x-self.y)

    def reset(self):
        self.move(0,0)
    def move(self,newx,newy):
        self.x=newx
        self.y=newy
    def movX(self,newx):
        self.x=newx
    def movY(self,newy):
        self.x=newy
    def showPoint(self):
        return f'({self.x},{self.y})'

## Main Program ##
from random import randint
def addPoints(p1,p2):
    return Point(p1.x+p2.x,p1.y+p2.y)

l1 = [Point(randint(1,5),randint(1,5)) for _ in range(5)]
l2 = [Point(randint(1,2),randint(1,2)) for _ in range(5)]

for i in l1 :    
    print(i.showPoint())
for i in l2 :    
    print(i.showPoint())

l3=list(map(addPoints,l1,l2))

for p in l3:
    print(p.showPoint())
l3.sort(key=lambda p: p.mag)
print('--'*10)
for p in l3:
    print(p.showPoint())

l4=list(map(addPoints,l1,l2))

for p in l4:
    print(p.showPoint())
l4.sort(key=lambda p: p.res())
print('--'*20)
for p in l4:
    print(p.showPoint())

