n = int(input())
ds = list(map(int,input().split()))
sum = sum(ds) // n
kq = 100000000
gt = 0
for i in ds:
    sum = 0
    for j in ds:
        sum += abs(j-i)
    if sum<kq:
        kq = min(kq,sum)
        gt = i
print(kq,gt)
    
