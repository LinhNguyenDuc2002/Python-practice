import bisect
while True:
    a = list(map(int,input().split()))
    if a[0]==-1:
        break
    else:
        l,r = a[0],a[1]
        n = int(input())
        ds = list(range(2,n+1))
        s = set()
        i = 1
        while i<=r//2+1:
            a = [j*i for j in ds]
            x = bisect.bisect_left(a,l)
            y = bisect.bisect_right(a,r)
            s.update(a[x:y])
            i += 1
        cnt = (r-l+1)-len(s)
        if cnt>0:
            print(cnt)
        else:
            print(0)