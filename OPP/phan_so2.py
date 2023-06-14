import math
class PS:
    def __init__(self,t,m) -> None:
        self.m = m
        self.t = t
    def toi_gian(self):
        a = math.gcd(self.m,self.t)
        self.m //= a
        self.t //= a
    def __add__(self,ps):
        x = self.t*ps.m + ps.t*self.m
        y = self.m*ps.m
        return PS(x,y)
    def __str__(self) -> str:
        # return str(self.t) + "/" + str(self.m)
        # return "{0}/{1}".format(self.t,self.m)
        return f"{self.t}/{self.m}"
ps = list(map(int,input().split()))
a = PS(ps[0],ps[1])
b = PS(ps[2],ps[3])
a.toi_gian()
b.toi_gian()
c = a+b # sử dụng nạp chồng tử
c.toi_gian()
print(c)