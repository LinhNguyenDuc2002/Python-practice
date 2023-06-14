def check(ds1,ds2):
    for i in range(0,len(ds1)):
        if ds1[i]>ds2[i]:
            return False
    return True
test = int(input())
while test > 0:
    n = int(input())
    ds1 = list(map(int,input().split()))
    ds2 = list(map(int,input().split()))
    ds1.sort()
    ds2.sort()
    if check(ds1,ds2):
        print("YES")
    else:
        print("NO")
    test -= 1