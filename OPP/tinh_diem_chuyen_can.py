import collections
class SinhVien:
    def __init__(self,id,name,classroom) -> None:
        self.id = id
        self.name = name
        self.classroom = classroom
        self.mark = 10
    def xuly(self,s):
        ds = collections.Counter(s)
        self.mark -= ds['v']*2
        self.mark -= ds['m']
    def __str__(self) -> str:
        if self.mark>0:
            return self.id + " " + self.name + " " + self.classroom + " " + str(self.mark)
        else:
            return self.id + " " + self.name + " " + self.classroom + " 0 " + "KDDK"
test = int(input())
ds = dict()
t = test
while test > 0:
    a = SinhVien(input(),input(),input())
    ds[a.id] = a
    test -= 1
while t > 0:
    a = list(input().split())
    ds[a[0]].xuly(a[1])
    t -= 1
for i in ds:
    print(ds[i])
