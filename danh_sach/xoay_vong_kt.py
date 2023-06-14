test = int(input())
ds = list()
while test > 0:
    ds.append(input())
    test -= 1
count = 0
while True:
    count += 1
    for i in range(len(ds)):
        ds[i] = ds[i][1:]+ds[i][0]
    print(ds)
    s = set(ds)
    if len(s) == 1:
        break
print(count)

