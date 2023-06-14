from decimal import Decimal
import math
class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def distance(self,p):
        a = (self.x-p.x)**2
        b = (self.y-p.y)**2
        return math.sqrt(a+b)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1