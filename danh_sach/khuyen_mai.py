n,k = map(int,input().split())
trc = list(map(int,input().split()))
sau = list(map(int,input().split()))
gia = dict()
for i in range(n):
    gia[i] = sau[i]-trc[i]
gia = sorted(gia.items(),key=lambda x : (-x[1]))
sum = 0
count = 0
for i in gia:
    if count<k:
        sum += trc[i[0]]
        count += 1
    else:
        if trc[i[0]]<sau[i[0]]:
            sum += trc[i[0]]
        else:
            sum += sau[i[0]]
print(sum)
