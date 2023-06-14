test = int(input())
while test > 0:
    n = int(input())
    ds = list(map(int,input().split()))
    l,r = [0]*n,[0]*n
    l[0], r[-1] = ds[0], ds[-1]
    for i in range(1, n):
        l[i] = max(l[i-1], ds[i])
    for i in range(n-2, -1, -1):
        r[i] = min(r[i+1], ds[i])
    count = len([ds[i] for i in range(1, n-1) if  l[i-1] <= ds[i] and r[i+1] > ds[i]])
    if ds[0] < r[1]: count += 1
    if ds[-1] >= l[-2]:  count += 1
    print(count)
    test -= 1