import datetime
class KhachHang:
    def __init__(self,id,name,room,old,new,dv) -> None:
        self.id = 'KH'+'{:02d}'.format(id)
        self.name = name
        self.room = room
        self.sum = dv
        old = datetime.datetime.strptime(old,"%d/%m/%Y")
        new = datetime.datetime.strptime(new,"%d/%m/%Y")
        self.kc = (new-old).days+1
        if self.room[0]=='1':
            self.sum += self.kc*25
        elif self.room[0]=='2':
            self.sum += self.kc*34
        elif self.room[0]=='3':
            self.sum += self.kc*50
        else:
            self.sum += self.kc*80
        
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + self.room + " " + str(self.kc) + " " + str(self.sum)
test = int(input())
t = 1
ds = list()
while t <=test:
    a = KhachHang(t,input().strip(),input().strip(),input().strip(),input().strip(),int(input()))
    ds.append(a)
    t += 1
ds.sort(key=lambda x : (-x.sum,x.id))
for i in ds:
    print(i)
