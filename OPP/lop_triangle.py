import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,p):
        a = self.x-p.x
        b = self.y-p.y
        return math.sqrt(a*a+b*b)
    
class Triangle:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def cnt(self):
        a = self.x.distance(self.y)
        b = self.x.distance(self.z)
        c = self.y.distance(self.z)
        if max(a,b,c)*2 >= (a+b+c):
            print("INVALID")
        else:
            p = (a+b+c)
            s = math.sqrt(p*(p-2*c)*(p-2*a)*(p-2*b))*1/4
            print(f'{s:.2f}')

l = []
i = 0
for _ in range(int(input())):
    l += list(map(float, input().split()))
    A = Point(l[i], l[i + 1])
    B = Point(l[i + 2], l[i + 3])
    C = Point(l[i + 4], l[i + 5])
    tri = Triangle(A, B, C)
    tri.cnt()
    i += 6