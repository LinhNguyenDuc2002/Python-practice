def find_min(x,a,b):
    kq = ''
    for i in range(0,len(x)):
        if x[i]== b:
            kq += a
        else:
            kq += x[i]
    return kq
def find_max(x,a,b):
    kq = ''
    for i in range(0,len(x)):
        if x[i]==a:
            kq += b
        else:
            kq += x[i]
    return kq
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
    a = find_min(x1,n,k)
    b = find_min(x2,n,k)
    print(int(a)+int(b),end = ' ')
    a = find_max(x1,n,k)
    b = find_max(x2,n,k)
    print(int(a)+int(b))
    test -= 1