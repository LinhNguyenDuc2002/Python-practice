import re
import collections
test = int(input())
ds = list()
while test > 0:
    s = input().lower()
    s = re.sub("\W"," ",s)
    s = re.sub("\d"," ",s)
    ds+=s.split()
    test -= 1
count = collections.Counter(ds)
a = sorted(count.items(),key=lambda x : (-x[1],x[0]))
for i in a:
    print(*i)
