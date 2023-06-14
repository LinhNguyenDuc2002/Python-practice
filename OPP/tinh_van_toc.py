import datetime
from decimal import Decimal, ROUND_HALF_UP
class vantoc:
    def __init__(self,name,city,hour) -> None:
        self.name = name
        self.city = city
        hours = datetime.datetime.strptime(hour,"%H:%M")
        a = datetime.datetime.strptime("06:00","%H:%M")
        self.tg = (hours-a).seconds/3600
        self.id = self.format(name,city)
        self.vantoc = 120/self.tg
    def format(self,name,city):
        s = ''
        name = name.split()
        city = city.split()
        for i in city:
            s += i[0]
        for i in name:
            s += i[0]
        return s
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + self.city + " " + str(Decimal(self.vantoc).quantize(0, rounding=ROUND_HALF_UP)) + " Km/h"
test = int(input())
ds = list()
while test > 0:
    a = vantoc(input(),input(),input())
    ds.append(a)
    test -= 1
ds.sort(key=lambda x : x.vantoc,reverse=True)
for i in ds:
    print(i)
    