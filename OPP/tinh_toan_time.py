import datetime
class TG:
    def __init__(self,id,name,old,new) -> None:
        self.id = id
        self.name = name
        old = datetime.datetime.strptime(old,'%H:%M')
        new = datetime.datetime.strptime(new,'%H:%M')
        tg = str(new-old)
        a = list(map(int,tg.split(':')))
        self.hour = a[0]
        self.minutes = a[1]
    def __str__(self) -> str:
        return self.id + "  " + self.name + " " + str(self.hour) + " gio " + str(self.minutes) + " phut"
test = int(input())
ds = list()
while test > 0:
    a = TG(input(),input(),input(),input())
    ds.append(a)
    test -= 1
ds.sort(key=lambda x : (-x.hour,-x.minutes))
for i in ds:
    print(i)
