import collections
test = int(input())
n = test
ds = list()
while test > 1:
    ds += input().split()
    test -= 1
a = collections.Counter(ds)
a = sorted(a.items(),key=lambda x : x[1], reverse=True)
check = False
if a[0][1] == n - 1:
    for i in range(1,len(a)):
        if a[i][1] != 1:
            check = True
            break
else:
    check = True
if check:
    print('No')
else:
    print('Yes')