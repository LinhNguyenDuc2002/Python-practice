import datetime
class DanhBa:
    def __init__(self,name,sdt,day) -> None:
        self.name = name
        a = name.split()
        self.lname = a[len(a)-1]
        self.fname = a[0:len(a)-1]
        self.sdt = sdt
        self.day = day
    def __str__(self) -> str:
        return self.name + ": " + self.sdt + " " + datetime.datetime.strftime(self.day,"%d/%m/%Y")
ds = list()
content=list()
with open("File/SOTAY.txt","r") as file:
    for line in file:
        content.append(line.strip())
    file.close()
i = 0
while i<len(content):
    try:
        a = datetime.datetime.strptime(content[i].split()[1],"%d/%m/%Y")
        day = a
        i += 1
    except:
        a = DanhBa(content[i],content[i+1],day)
        ds.append(a)
        i += 2
ds.sort(key=lambda x : (x.lname,x.fname))
with open("File/DIENTHOAI.txt","w") as file:
    for i in ds:
        file.write(i.__str__()+"\n")
