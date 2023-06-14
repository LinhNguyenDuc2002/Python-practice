def convert(a,i):
    kq = ''
    while a>0:
        if (a%i)>=10:
            kq = chr(55+a%i) + kq
        else:
            kq = str(a%i)+kq
        a //=i
    return kq

a = list()
with open("./File/DATA.in","r") as file:
    for line in file:
        a.append(line.strip())
test = int(a[0])
i = 1
while test > 0:
    x = int(a[i])
    s = a[i+1]
    if x!=2:
        k = int(s,2)
        print(convert(k,x))
    else:
        print(s)
    i+=2
    test -=1