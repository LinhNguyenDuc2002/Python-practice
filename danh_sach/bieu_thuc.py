test = int(input())
while test > 0:
    mo = [0,]
    dong = [0,]
    s = input()
    m = 0
    for i in s:
        if i=='(':
            m += 1
            mo.append(m)
            print(m,end=' ')
        elif i==')':
            d = m
            while d>0:
                if d not in dong:
                    dong.append(d)
                    print(d,end=' ')
                    break
                d -= 1
    print()
    test -= 1