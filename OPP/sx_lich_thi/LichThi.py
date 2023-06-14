from Monthi import MonThi
from CaThi import CaThi
class LichThi:
    def __init__(self,idca,idmon,idgroup,sv) -> None:
        self.ca = ds_ca[idca]
        self.mon = ds_mon[idmon]
        self.idgroup = idgroup
        self.sv = sv
    def __str__(self) -> str:
        return str(self.ca) + " " + str(self.mon) + " " + self.idgroup + " " + self.sv

if __name__ == '__main__':
    global ds_mon
    global ds_ca
    lich = list()
    ds_mon = dict()
    ds_ca = dict()
    with open('OPP/sx_lich_thi/MONTHI.in') as file:
        a = list()
        for line in file:
            a.append(line)
        test = int(a[0])
        i = 1
        while test > 0:
            x = MonThi(a[i].strip(),a[i+1].strip(),a[i+2].strip())
            ds_mon[x.id] = x
            i += 3
            test -= 1
    with open('OPP/sx_lich_thi/CATHI.in') as file:
        a = list()
        for line in file:
            a.append(line)
        test = int(a[0])
        i = 1
        t = 1
        while t <= test:
            x = CaThi(t,a[i].strip(),a[i+1].strip(),a[i+2].strip())
            ds_ca[x.id] = x
            i += 3
            t += 1
    with open('OPP/sx_lich_thi/LICHTHI.in') as file:
        a = list()
        for line in file:
            a.append(line)
        test = int(a[0])
        i = 1
        while test > 0:
            s = list(a[i].split())
            x = LichThi(s[0],s[1],s[2],s[3])
            lich.append(x)
            i += 1
            test -= 1
lich.sort(key=lambda x : (x.ca.date,x.ca.hour,x.ca.id))
for i in lich:
    print(i)
