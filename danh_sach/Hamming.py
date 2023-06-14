import math
import bisect, sys
test = int(input())
ds = [1,]
i = 0
for line in sys.stdin:
    a = int(line)
    if a<=ds[i]:
        if a in ds:
            print(ds.index(a)+1)
        else:
            print("Not in sequence")
    else:
        x = ds[i]
        while a>ds[i]:
            if x*2 not in ds:
                ds.append(x*2)
            if x*3 not in ds:
                ds.append(x*3)
            if x*5 not in ds:
                ds.append(x*5)
            ds.sort()
            i += 1
            x = ds[i]
        if a in ds:
            print(ds.index(a)+1)
        else:
            print("Not in sequence")
    test -= 1
    if test==0: break