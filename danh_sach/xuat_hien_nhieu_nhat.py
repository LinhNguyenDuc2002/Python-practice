import collections
test = int(input())
while test > 0:
    n = int(input())
    mydict = collections.Counter(map(int,input().split()))
    a = max(mydict.values())
    mydict = sorted(mydict.items(), key = lambda x:x[0])
    if a>n//2:
        for i in mydict:
            if i[1]==a:
                print(i[0])
                break
    else:
        print("NO")
    test -= 1
