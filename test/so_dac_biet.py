import math,itertools
mod = 1000000007
def power(n,a):
    if a==0:
        return 1
    x = power(n,a//2)
    x = (x*x)%mod
    if a%2!=0:
        x = (x*n)%mod
    return x%mod
test = int(input())
while test > 0:
    n,m = map(int,input().split())
    i = 1
    sum = 0
    while sum<m:
        sum = 0
        for j in range(1,i):
            sum += math.comb(i,j)
        i += 1
    ds = list(x for x in range(i))
    a = list()
    kq = list()
    for i in range(len(ds)):
        a+=list(itertools.combinations(ds,i))
    a.remove(a[0])
    for i in a:
        sum = 0
        for j in i:
            sum+=power(n,j)
            sum%=mod
        kq.append(sum%mod)
    kq.sort()
    print(kq[m-1])
    test -= 1