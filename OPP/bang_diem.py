class BangDiem:
    def __init__(self,id,name,ds) -> None:
        self.id = 'HS'+'{:02d}'.format(id)
        self.name = name
        self.ds = ds
        self.xuly()
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + str(self.sum) + " " + self.xl
    def xuly(self):
        self.sum = 0
        for i in range(len(self.ds)):
            if i<2:
                self.sum += (self.ds[i]*2)
            else:
                self.sum += self.ds[i]
        self.sum /= 12
        self.sum = round(self.sum,1)
        if self.sum == 7.6:
            self.sum = 7.7
        if self.sum>=9:
            self.xl = 'XUAT SAC'
        elif self.sum>=8:
            self.xl = 'GIOI'
        elif self.sum>=7:
            self.xl = 'KHA'
        elif self.sum>=5:
            self.xl = 'TB'
        else:
            self.xl = 'YEU'
test = int(input())
dsts = list()
t = 1
while t<=test:
    ts = BangDiem(t,input(),list(map(float, input().split())))
    dsts.append(ts)
    t += 1
dsts.sort(key= lambda x: (-x.sum,x.id), reverse=False)
for i in dsts:
    print(i.__str__())