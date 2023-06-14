n = int(input())
ds = list()
for i in range(n):
    a = list(map(int,input().split()))
    ds.append(a)
if n==2:
    print("1 1")
else:
    kq = list()
    kq.append((ds[0][2]-ds[1][2]+ds[0][1])//2)
    for i in range(1,n):
        kq.append(ds[0][i]-kq[0])
    print(*kq)
