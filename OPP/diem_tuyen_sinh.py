def chuan_hoa(n):
    a = n.split()
    kq = ''
    for i in a:
        kq = kq+i+" "
    return kq.strip()
class sv:
    def __init__(self,id,name,mark,dt,kv) -> None:
        self.id = "TS"+'{:02d}'.format(id)
        self.name = chuan_hoa(name).title()
        self.mark = mark
        if kv=='1':
            self.mark += 1.5
        elif kv=='2':
            self.mark += 1
        if dt!='Kinh':
            self.mark += 1.5
        if self.mark >= 20.5:
            self.tt = 'Do'
        else:
            self.tt = 'Truot'
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + '{:.1f}'.format(self.mark) + " " + self.tt
test = int(input())
ds = list()
t = 1
while t <= test:
    a = sv(t,input().strip(),float(input()),input().strip(),input().strip())
    ds.append(a)
    t += 1
ds.sort(key=lambda x : (-x.mark,x.id))
for i in ds:
    print(i)
