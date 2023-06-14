import datetime
class LuongMua:
    def __init__(self,id,name) -> None:
        self.id = "T" + "{:02d}".format(id)
        self.name = name
        self.solg = 0
        self.tg = 0
    def xuLy(self, start, end, solg):
        date1 = datetime.datetime.strptime(start,"%H:%M")
        date2 = datetime.datetime.strptime(end,"%H:%M")
        self.solg += solg
        self.tg += (date2-date1).seconds/3600 # đổi ra giờ
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + "{:.2f}".format(self.solg/self.tg)
test = int(input())
ds = dict()
t = 1
while test > 0:
    name = input()
    start = input()
    end = input()
    solg = int(input())
    if name in ds:
        ds[name].xuLy(start,end,solg)
    else:
        ds[name] = LuongMua(t,name)
        ds[name].xuLy(start,end,solg)
        t += 1
    test -= 1
for i in ds:
    print(ds[i])
