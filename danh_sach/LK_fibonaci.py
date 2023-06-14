test = int(input())
while test > 0:
    a,b = map(int,input().split())
    ds = list()
    ds.append(1)
    ds.append(1)
    for i in range(2,b):
        ds.append(ds[i-1]+ds[i-2])
    for i in range(a,b+1):
        print(ds[i-1], end = ' ')
    print()
    test -= 1