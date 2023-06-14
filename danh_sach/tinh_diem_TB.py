n = int(input())
ds = list(map(float,input().split()))
ds.sort()
sum = 0
count = 0
for i in ds:
    if i!=ds[0] and i!=ds[len(ds)-1]:
        sum += i
        count += 1
sum /= count
print("%.2f" % sum)