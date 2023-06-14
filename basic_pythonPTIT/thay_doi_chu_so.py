test = int(input())
while test >0:
    a = list(map(int,input().split()))
    n = str(min(a))
    k = str(max(a))
    s = input()
    try:
        x1,x2 = s.split()
    except:
        x1 = s
        x2 = input()
    a = x1.replace(k,n)
    b = x2.replace(k,n)
    print(int(a)+int(b),end = ' ')
    a = x1.replace(n,k)
    b = x2.replace(n,k)
    print(int(a)+int(b))
    test -= 1