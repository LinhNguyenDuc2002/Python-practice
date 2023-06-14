import math
import sys
import bisect
def find(n):
    s = set()
    s.add(1)
    s.add(n)
    for j in range(2,int(math.sqrt(n))+1):
        if n%j==0:
            s.add(j)
            s.add(n//j)
    return len(s)

test = int(input())
ds = [1,]
m = 1
index = 0
hs = 2
x = 2
n = 10000000
while ds[len(ds)-1]<=n:
    i = ds[index]*x
    if i not in ds:
        length = find(i)
        if(length>m):
            m = length
            ds.append(i)
            x += 1
            hs = max(hs,x)
        else:
            if x>=hs:
                index += 1
                x = 2
            else:
                x += 1
    else:
        x += 1
        hs = max(hs,x)
for line in sys.stdin:
    n = int(line)
    print(ds[bisect.bisect_left(ds,n)])
    test -= 1
    if test==0: break

# import sys
# from bisect import bisect_left
# a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
# t = int(input())
# i = 0
# for line in sys.stdin :
#     n = int(line)
#     print(a[bisect_left(a, n)])
#     i += 1
#     if i == t:  break