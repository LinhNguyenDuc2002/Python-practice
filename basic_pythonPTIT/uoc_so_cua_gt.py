test = int(input())
while test > 0:
    n,p = map(int,input().split())
    i = 1
    while p*i<=n:
        i += 1
    count = 0
    for j in range(p*(i-1),0,-p):
        while j%p==0:
            count +=1
            j/=p
    print(count)
    test -= 1