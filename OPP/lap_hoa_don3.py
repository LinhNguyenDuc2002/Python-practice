import datetime
class KhachHang:
    def __init__(self,id,name,solg,dgia,chiet) -> None:
        self.id = id
        self.name = name
        self.solg = solg
        self.dgia = dgia
        self.chiet = chiet
        self.sum = self.solg*self.dgia - self.chiet
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + str(self.solg) + " " + str(self.dgia) + " " + str(self.chiet) + " " + str(self.sum)
test = int(input())
ds = list()
t = 1
while t <=test:
    a = KhachHang(input(),input(),int(input()),int(input()),int(input()))
    ds.append(a)
    t += 1
ds.sort(key=lambda x : (-x.sum,x.id))
for i in ds:
   print(i)
