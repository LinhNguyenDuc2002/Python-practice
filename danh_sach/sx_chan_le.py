n = int(input())
ds = list()
while len(ds)<n:
    a = (map(int,input().split()))
    for i in a:
        ds.append(i)
ds1 = list()
ds2 = list()
for i in ds:
    if i%2==0:
        ds1.append(i)
    else:
        ds2.append(i)
ds1.sort()
ds2.sort(reverse=True)
x = y = 0
for i in ds:
    if i%2==0:
        print(ds1[x],end = ' ')
        x += 1
    else:
        print(ds2[y],end = ' ')
        y += 1