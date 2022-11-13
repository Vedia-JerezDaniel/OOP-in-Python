from Task3 import Point
from random import randint

## TASK 3
p1=Point(4,5)
p2=Point(1,2)
print(p1.__abs__())
# p1.reset()
# # print(abs(p1))
# print(-p1)
# p1-=p2
print(p2*2)
print(p1*p2)
# p1/=2
# # print(p1)
print(p1>=p2)

p1.__mults__()
# for component in p1:
#     print(component)

## TASK 4

l = [Point(randint(-4,5),randint(-1,2)) for _ in range(10)]
print(l)
ringPoints=list(filter(lambda p:4 >= abs(p) >= 3 ,l))
print(ringPoints)
bigringPoints=[p*5 for p in ringPoints]
print(bigringPoints)
p1=Point(5,10)
newList=[p1*p for p in bigringPoints]
print(newList)


