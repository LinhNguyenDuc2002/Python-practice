import collections
test = int(input())
while test > 0:
    n = int(input())
    ds = map(int,input().split())
    a = collections.Counter(ds)
    for i in a:
        if a.get(i)%2!=0:
            print(i)
    test -= 1