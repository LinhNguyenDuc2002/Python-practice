test = int(input())
while test > 0:
    n,k = map(int,input().split())
    sum = 0
    for i in range(1,n+1):
        sum += (i**k)
        sum %= ((10**9)+1)
    print(sum)
    test -= 1