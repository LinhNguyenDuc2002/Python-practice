test = int(input())
while test > 0:
    m,n = map(int,input().split())
    ds = list()
    for i in range(m):
        a = list(map(int,input().split()))
        ds.append(a)
    kq = list()
    for i in range(m):
        a = list()
        for k in range(m):
            sum = 0
            for j in range(n):
                sum += (ds[i][j]*ds[k][j])
            a.append(sum)
        kq.append(a)
    for i in kq:
        print(*i)
    test -= 1