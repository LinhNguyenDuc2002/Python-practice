import math, collections
n = int(input())
ds = list()
count  = 0
for i in range(n):
    s = input()
    a = list(s[::1])
    ds.append(a)
for i in range(n):
    a = collections.Counter(ds[i])
    count += math.comb(a['C'],2)
for i in range(n):
    sum = 0
    for j in range(n):
        if ds[j][i] == 'C':
            sum += 1
    count += math.comb(sum,2)
print(count)
