test = int(input())
while test > 0:
    m,n = map(int,input().split())
    ds = list(map(int,input().split()))
    mmax = max(ds)
    kq = list()
    for i in range(m):
        if ds[i]==mmax:
            kq = ds[0:i]
            kq.append(n)
            kq += ds[i:]
            break
    m = ''
    n = ''
    for i in kq:
        if i<0:
            m = m + str(i) + ' '
        else:
            n = n + str(i) + ' '
    print(m+n)
    test -= 1