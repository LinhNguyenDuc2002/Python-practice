import math
class PS:
    def __init__(self,t,m) -> None:
        self.m = m
        self.t = t
    def toi_gian(self):
        a = math.gcd(self.m,self.t)
        self.m //= a
        self.t //= a
    def __str__(self) -> str:
        return str(self.t) + "/" + str(self.m)
t,m = map(int,input().split())
a = PS(t,m)
a.toi_gian()
print(a)


