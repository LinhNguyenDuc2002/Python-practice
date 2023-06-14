n = int(input())
ds = list(map(int,input().split()))
count = 0
for i in range(0,len(ds)):
    for j in range(i+1,len(ds)):
        if ds[j]<ds[i]:
            count += 1
print(count)
