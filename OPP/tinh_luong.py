class Phong:
    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name
class nv:
    def __init__(self,id,name,luong,cong) -> None:
        self.id = id
        self.name = name
        self.luong = luong*cong
        k = int(self.id[1:3])
        if self.id.startswith('A'):
            if k<=3:
                self.luong *= 10
            elif k<=8:
                self.luong *= 12
            elif k<=15:
                self.luong *= 14
            else:
                self.luong *= 20
        elif self.id.startswith('B'):
            if k<=3:
                self.luong *= 10
            elif k<=8:
                self.luong *= 11
            elif k<=15:
                self.luong *= 13
            else:
                self.luong *= 16
        elif self.id.startswith('C'):
            if k<=3:
                self.luong *= 9
            elif k<=8:
                self.luong *= 10
            elif k<=15:
                self.luong *= 12
            else:
                self.luong *= 14
        else:
            if k<=3:
                self.luong *= 8
            elif k<=8:
                self.luong *= 9
            elif k<=15:
                self.luong *= 11
            else:
                self.luong *= 13
        self.room_name = dsp[self.id[3:]].name
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + self.room_name + " " + str(self.luong*1000)
test = int(input())
dsp = dict()
while test > 0:
    s = input().split(" ",1)
    a = Phong(s[0],s[1])
    dsp[a.id] = a
    test -= 1
test = int(input())
ds = list()
while test > 0:
    a = nv(input(),input(),int(input()),int(input()))
    ds.append(a)
    test -= 1
for i in ds:
    print(i)
