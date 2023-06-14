class KhachHang:
    def __init__(self,id,name,old,new) -> None:
        self.id = 'TS0'+str(id)
        self.name = name
        if old > 10:
            old /=10
        if new > 10:
            new /= 10
        self.tb = (old+new)/2
        if self.tb < 5:
            self.xl = 'TRUOT'
        elif self.tb < 8 :
            self.xl = 'CAN NHAC'
        elif self.tb <= 9.5:
            self.xl = 'DAT'
        else:
            self.xl = 'XUAT SAC'


        
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + '{:.2f}'.format(self.tb) + " " + self.xl
test = int(input())
t = 1
ds = list()
while t <=test:
    a = KhachHang(t,input(),float(input()),float(input()))
    ds.append(a)
    t += 1
ds.sort(key=lambda x : (-x.tb,x.id))
for i in ds:
    print(i)

