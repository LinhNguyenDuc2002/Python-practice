def ch(name):
    a = list(name.split())
    kq = ""
    for i in a:
        kq+=i.title()+" "
    return kq.strip()
class KhachHang:
    def __init__(self,id,name,type,dau,cuoi) -> None:
        self.id = "KH"+"{:02d}".format(id)
        self.name = ch(name)
        self.type = type
        self.dau = dau
        self.cuoi = cuoi
        if type=='A':
            self.dm = 100
        elif type=='B':
            self.dm=500
        else: self.dm = 200
        if cuoi-dau<self.dm:
            self.indm = (cuoi-dau)*450
        else:
            self.indm = self.dm*450
        if cuoi-dau > self.dm:
            self.outdm = (cuoi-dau-self.dm)*1000
        else:
            self.outdm = 0
        self.vat = self.outdm//20
        self.sum = self.indm+self.outdm+self.vat
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + str(self.indm) + " " + str(self.outdm) + " " + str(self.vat) + " " + str(self.sum)

test = int(input())
ds = list()
i = 1
while i<=test:
    name = input()
    k = input().split()
    a = KhachHang(i,name,k[0],int(k[1]),int(k[2]))
    ds.append(a)
    i += 1
ds.sort(key=lambda x:x.sum,reverse=True)
for i in ds:
    print(i)
