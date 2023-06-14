import collections
test = int(input())
while test > 0:
    n = int(input())
    ds = list()
    for i in range(n):
        ds.append(int(input()))
    mydict = collections.Counter(ds)
    mydict = sorted(mydict.items(),key = lambda x:(-x[1],x[0]) )
    print(mydict[0][0])
    test -= 1
