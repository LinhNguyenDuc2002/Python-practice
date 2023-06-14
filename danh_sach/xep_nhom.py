test = int(input())
while test > 0:
    n,k = map(int,input().split())
    ds = list(map(int,input().split()))
    ds.sort()
    count = 0
    while len(ds)>=k:
        l = len(ds)-k
        a = ds[l:]
        # print("a=",a)
        count += 1
        a = [i-1 for i in a if i-1>0]
        ds = ds[0:l]+a
        ds.sort()
        # print("ds=",ds)
    print(count)
    test -= 1
