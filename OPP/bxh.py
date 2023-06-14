class sv():
    def __init__(self,name,x,y) -> None:
        self.name = name
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'{self.name} {self.x} {self.y}'
    
n = int(input())
ds = list()
while n > 0:
    name = input()
    a = list(map(int,input().split()))
    s = sv(name, a[0], a[1])
    ds.append(s) 
    n -= 1
ds = sorted(ds,key= lambda x: (-x.x,x.y,x.name))
print(*ds,sep="\n")