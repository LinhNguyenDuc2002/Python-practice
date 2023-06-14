import collections
test = int(input())
s = set()
smaller = dict()
d = dict()
while test > 0:
    a = input().split()
    s.add(a[0])
    s.add(a[2])
    if a[1]=='>':
        d[a[2]] = d.setdefault(a[2],0)+1
        if smaller.get(a[0])==None:
            smaller[a[0]] = list()
        smaller[a[0]].append(a[2])
    else:
        d[a[0]] = d.setdefault(a[0],0)+1
        if smaller.get(a[2])==None:
            smaller[a[2]] = list()
        smaller[a[2]].append(a[0])
    test -= 1
kq = collections.deque()
for i in s:
    if d.get(i)==None: kq.append(i)
count = 0
while len(kq)>0:
    a = kq.popleft()
    count += 1
    if smaller.get(a)!=None:
        for i in smaller[a]:
            if d.get(i)!=None:
                d[i] -= 1
                if d[i] == 0:
                    kq.append(i)
print('impossible' if count!=len(s) else 'possible')