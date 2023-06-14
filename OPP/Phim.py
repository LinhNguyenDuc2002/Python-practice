import datetime
class TheLoai:
    def __init__(self,id,theloai) -> None:
        self.id = "TL"+'{:03d}'.format(id)
        self.theloai = theloai

    def __str__(self) -> str:
        return self.theloai
class Phim:
    def __init__(self,id,TL,date,name,series) -> None:
        self.id = 'P'+'{:03d}'.format(id)
        self.TL = TL
        self.date = datetime.datetime.strptime(date,'%d/%m/%Y')
        self.name = name
        self.series = series
    def __str__(self) -> str:
        return self.id + " " + self.TL.__str__() + " " + datetime.datetime.strftime(self.date,'%d/%m/%Y')\
                + " " + self.name + " " + str(self.series)
if __name__ == '__main__': 
    n,m = map(int,input().split())
    dsTheLoai = dict()
    ds = list()
    for i in range(n):
        a = TheLoai(i+1,input())
        dsTheLoai[a.id] = a
    for i in range(m):
        a = Phim(i+1,dsTheLoai[input()],input(),input(),int(input()))
        ds.append(a)
    ds.sort(key=lambda x : (x.date,x.name,-x.series))
    for i in ds:
        print(i)
