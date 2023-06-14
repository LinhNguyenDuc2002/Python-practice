from datetime import *
class MonHoc:
    def __init__(self,id,name) -> None:
        self.id =id
        self.name = name
    def __str__(self) -> str:
        return self.id + " " + self.name
class LichThi:
    def __init__(self,id,mon,day,hour,group) -> None:
        self.id = "T"+'{:03d}'.format(id)
        self.mon = mon
        self.day = datetime.strptime(day,"%d/%m/%Y")
        self.hour = datetime.strptime(hour,"%H:%M")
        self.group = group
    def __str__(self) -> str:
        return self.id + " " + self.mon.__str__() + " " + datetime.strftime(self.day,"%d/%m/%Y") + " " + datetime.strftime(self.hour,"%H:%M") + " " + self.group

if __name__ == '__main__':
    n,m = map(int,input().split())
    dsMon = dict()
    ds = list()
    for i in range(n):
        a = MonHoc(input(),input())
        dsMon[a.id] = a
    for i in range(m):
        x = input().split()
        a = LichThi(i+1,dsMon[x[0]],x[1],x[2],x[3])
        ds.append(a)
    ds.sort(key=lambda x : (x.day,x.hour,x.mon.id))
    for i in ds:
        print(i)
