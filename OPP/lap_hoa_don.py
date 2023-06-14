class KhachHang:
    def __init__(self,id,name,old,new) -> None:
        self.id = 'KH'+'{:02d}'.format(id)
        self.name = name
        kc = new - old
        self.sum = 0
        if kc<=50:
            a = 2
        elif kc<=100:
            a = 3
        else:
            a = 5
        if kc>50:
            self.sum += 50*100
            kc -= 50
            if kc>50:
                self.sum += 50*150
                kc -= 50
                self.sum += kc*200
            else:
                self.sum += kc*150
        else:
            self.sum += kc*100
        self.sum += self.sum*a/100
        
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + str(round(self.sum))
test = int(input())
t = 1
ds = list()
while t <=test:
    a = KhachHang(t,input(),int(input()),int(input()))
    ds.append(a)
    t += 1
ds.sort(key=lambda x : (-x.sum,x.id))
for i in ds:
    print(i)
