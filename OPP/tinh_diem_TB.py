import math
class SV:
    def __init__(self,id,name,diem1,diem2,diem3) -> None:
        self.id = "SV" + '{:02d}'.format(id)
        self.name = xuly(name)
        self.tb = (diem1*3+diem2*3+diem3*2)/8
    def setHang(self,i):
        self.hang = i
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + '{:.2f}'.format(math.ceil(self.tb * 100) / 100) + " " + str(self.hang)
def xuly(name):
    a = name.split()
    name = ''
    for i in a:
        name += i.title() + " "
    return name.strip()
test = int(input())
ds = list()
for i in range(test):
    a = SV(i+1,input(),int(input()),int(input()),int(input()))
    ds.append(a)
ds.sort(key=lambda x : -x.tb)
k = 1
for i in range(len(ds)):
    if i==0:
        ds[i].setHang(k)
    else:
        if ds[i].tb==ds[i-1].tb:
            ds[i].setHang(ds[i-1].hang)
        else:
            ds[i].setHang(k)
    k += 1
ds.sort(key=lambda x: (x.hang,x.id))
for i in ds:
    print(i)