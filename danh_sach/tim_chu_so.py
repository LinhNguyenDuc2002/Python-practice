import math
mod = 1000
class Pair:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return self.x + " " + self.y
def Tich(a,b):
    r = Pair(0,0)
    r.x = (a.x*b.x+5*a.y*b.y)%mod
    r.y = (a.x*b.y+a.y*b.x)%mod
    return r
def lt(a,b):
    if b==0:
        return Pair(1,0)
    if b&1:
        return Tich(lt(a,b-1),a)
    p = lt(a,b>>1)
    return Tich(p,p)
test = int(input())
t = 1
x = Pair(3,1)
while t <= test:
    n = int(input())
    print(f'Case #{t}: ',end='')
    print(str(lt(x,n).x*2%mod-1).zfill(3))
    t += 1