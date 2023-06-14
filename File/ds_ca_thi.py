import datetime
class CaThi:
    def __init__(self,id,day,hour,room) -> None:
        self.id = "C" + "{:03d}".format(id)
        self.day = datetime.datetime.strptime(day,"%d/%m/%Y")
        self.hour = datetime.datetime.strptime(hour,"%H:%M")
        self.room = room
    def __str__(self) -> str:
        day = datetime.datetime.strftime(self.day,"%d/%m/%Y")
        hour = datetime.datetime.strftime(self.hour,"%H:%M")
        return self.id + " " + day + " " + hour + " " + self.room

content = list()
with open("./File/CATHI.in","r") as file:
    for line in file:
        content.append(line.strip())
    file.close()
test = content[0]
ds = list()
t = 1
for i in range(1,len(content),3):
    a = CaThi(t,content[i],content[i+1],content[i+2])
    ds.append(a)
    t += 1
ds.sort(key=lambda x : (x.day,x.hour,x.id))
for i in ds:
    print(i)