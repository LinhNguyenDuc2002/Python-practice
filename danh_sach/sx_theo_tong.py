import collections
test = int(input())
while test > 0:
    n = int(input())
    ds = input().split()
    mydict = dict()
    for i in ds:
        l = list(map(int,i[0::1]))
        mydict.update([(int(i),sum(l))])
    mydict = sorted(mydict.items(),key = lambda x : (x[1],x[0]))
    for i in mydict:
        print(i[0], end =' ')
    print()
    test -= 1
