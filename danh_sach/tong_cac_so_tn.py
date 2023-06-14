global ds
ds = list()
def find(n,s,k):
    for i in range(k,0,-1):
        s.append(i)
        if sum(s)==n:
            a = s.copy()
            ds.append(a)
            s.pop()
        elif sum(s)<n:
            find(n,s,i)
            s.pop()
        else:
            s.pop()
test = int(input())
while test > 0:
    ds.clear()
    n = int(input())
    s = list()
    find(n,s,n)
    print(len(ds))
    for i in ds:
        print('(',end = '')
        print(*i,end = '')
        print(')',end = ' ')
    print()
    test -= 1