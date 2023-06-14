def tranfer(ds,n,m,i):
    kq = list()
    while n!=m:
        kq.append(ds[i])
        i += 2
        n -= 1
    if i%2!=0:
        kq += ds[i-1:]
    else:
        kq += ds[i:]
    return kq
n,m = map(int,input().split())
ds = list()
for i in range(n):
    a = list(map(int,input().split()))
    ds.append(a)
if m==n:
    for i in ds:
        print(*i)
elif n>m:
    kq = tranfer(ds,n,m,1)
    for i in kq:
        print(*i)
else:
    kq = list()
    for i in zip(*ds):
        kq.append(list(i))
    ds = tranfer(kq,m,n,0)
    kq.clear()
    for i in zip(*ds):
        kq.append(list(i))
    for i in kq:
        print(*i)
      

    


     