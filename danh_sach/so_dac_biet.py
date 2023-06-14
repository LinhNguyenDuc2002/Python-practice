mod = 1000000007
def pow (a,b):
    if b==0:
        return 1
    x = pow(a,b//2)
    x = (x*x)%mod
    if b%2!=0:
        x=(x*a)%mod
    return x%mod
def calculator(n,k):
    if k<=1:
        return k
    x = 0
    while (k>>x)^1:#5 3 0
        x += 1
    # print(f'k={k} x={x} 1<<x={1<<x} k^(1<<x) = {k^(1<<x)}')
    return (pow(n,x)+calculator(n,k^(1<<x)))%mod
test = int(input())
while test > 0:
    n,k = map(int,input().split())
    print(calculator(n,k))
    test -= 1