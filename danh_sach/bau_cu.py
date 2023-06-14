import collections
n,m = map(int,input().split())
s = collections.Counter(map(int,input().split()))
s = dict(s)
value = set(s.values())
s = sorted(s.items(),key=lambda x : (-x[1],x[0]))
print(s)
if len(value)<2:
    print('NONE')
else:
    for i in s:
        if i[1]<max(value):
            print(i[0])
            break