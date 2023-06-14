class Matrix:
    def __init__(self,n,m,ds) -> None:
        self.n = n
        self.m = m
        self.ds = ds
    def mul(self):
        kq = list()
        for i in range(0,self.n):
            a = list()
            for k in range(0,self.m):
                s = 0
                for j in range(0,self.m):
                    s += self.ds[i][j]*self.ds[k][j]
                a.append(str(s))
            kq.append(a)
        return kq
test = int(input())
while test>0:
    n,m = map(int,input().split())
    ds = list()
    for i in range(0,n):
        a = list(map(int,input().split()))
        ds.append(a)
    matrix = Matrix(n,m,ds)
    kq = matrix.mul()
    for i in kq:
        print(' '.join(i))
    test -=1