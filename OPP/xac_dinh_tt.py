import datetime
class gv:
    def __init__(self,id,name,tt,mark1,mark2) -> None:
        d = {'A':'TOAN','B':'LY','C':'HOA'}
        self.id = 'GV'+'{:02d}'.format(id)
        self.name = name
        self.sum = mark1*2+mark2
        self.sub = d[tt[0]]
        if tt.endswith('1'):
            self.sum += 2
        elif tt.endswith('2'):
            self.sum += 1.5
        elif tt.endswith('3'):
            self.sum += 1
        if self.sum>=18:
            self.tt = 'TRUNG TUYEN'
        else:
            self.tt = 'LOAI'
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + self.sub + " " + '{:.1f}'.format(self.sum) + " " + self.tt
test = int(input())
ds = list()
t = 1
while t <= test:
    a = gv(t,input(),input(),float(input()),float(input()))
    ds.append(a)
    t += 1
ds.sort(key=lambda x : x.sum,reverse=True)
for i in ds:
    print(i)
