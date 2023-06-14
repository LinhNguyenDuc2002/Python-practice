def convert(a,i):
    kq = ''
    while a>0:
        if (a%i)>=10:
            kq = chr(55+a%i) + kq
        else:
            kq = str(a%i)+kq
        a //=i
    return kq
test = int(input())
while test>0:
    i = int(input())
    s = input()
    a = int(s,2)
    print(convert(a,i))
    test -=1