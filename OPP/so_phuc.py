class SoPhuc:
    def __init__(self,t,a) -> None:
        self.a = a
        self.t = t
    def __add__(self,sp):
        x = self.a+sp.a
        y = self.t+sp.t
        return SoPhuc(y,x)
    def __mul__(self,sp):
        x = self.t*sp.t - self.a*sp.a
        y = self.a*sp.t + sp.a*self.t
        return SoPhuc(x,y)
    def __str__(self) -> str:
        return "{0} + {1}i".format(self.t,self.a) if self.a>0 else "{0} - {1}i".format(self.t,self.a*-1)
test = int(input())
while test > 0:
    a,b,c,d=map(int,input().split())
    A = SoPhuc(a,b)
    B = SoPhuc(c,d)
    C = (A+B)*A
    D = (A+B)*(A+B)
    print(f"{C}, {D}")
    test -= 1