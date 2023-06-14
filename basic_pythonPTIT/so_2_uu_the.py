import collections
test = int(input())
while test > 0:
    n = int(input())
    ds = ['1','2']
    kq = list()
    while len(kq)<n:
        count = collections.Counter(ds[0])
        if count['2']>(len(ds[0])//2):
            kq.append(ds[0])
        ds.append(ds[0]+'0')
        ds.append(ds[0]+'1')
        ds.append(ds[0]+'2')
        ds.remove(ds[0])
    print(*kq)
        
    test -= 1