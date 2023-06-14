def mark(a):
    if a>=39:
        return 9
    elif a>=37:
        return 8.5
    elif a>=35:
        return 8
    elif a>=33:
        return 7.5
    elif a>=30:
        return 7
    elif a>=27:
        return 6.5
    elif a>=23:
        return 6
    elif a>=20:
        return 5.5
    elif a>=16:
        return 5
    elif a>=13:
        return 4.5
    elif a>=10:
        return 4
    elif a>=7:
        return 3.5
    elif a>=5:
        return 3
    elif a>=3:
        return 2.5
    else:
        return 0
test = int(input())
while test > 0:
    ds = input().split()
    sum = mark(int(ds[0]))+mark(int(ds[1]))+float(ds[2])+float(ds[3])
    a = (sum/4) - (sum//4)
    if a<0.25:
        print((sum//4))
    elif a>=0.25 and a<0.75:
         print((sum//4)+0.5)
    else:
        print((sum//4)+1)
    test -= 1