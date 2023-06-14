import itertools
m,n = map(int,input().split())
ds = set(input().split())
ds = list(ds)
ds.sort()
combine = itertools.combinations(ds,n)
for i in combine:
    print(*i)