test = int(input())
while test > 0:
    s = input()
    ds = set(s[::1])
    a = list(s[::1])
    if len(ds)==1:
        print('-1')
    else:
        i = len(a)-1
        while a[i]>=a[i-1] and i>0:
            i -= 1
        if i>0:
            a[i],a[i-1] = a[i-1],a[i]
        if a[0] == '0':
            print('-1')
        else:
            print(''.join(a))
    test -= 1