import re
test = int(input())
ds = list()
while test > 0:
    s = input()
    ds+=(map(int,re.sub("\D"," ",s).split()))
    test -= 1
ds.sort()
print(*ds, sep = "\n")
