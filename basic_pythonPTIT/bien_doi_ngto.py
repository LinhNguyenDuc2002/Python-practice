import math
def checkPrime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
test = int(input())
ds = list(map(int,input().split()))
a = list()
for i in ds:
    if not checkPrime(i):
        a.append(i)
kq = 0
for i in a:
    up = down = i
    count = 100000000
    while True:
        if checkPrime(up+1):
            count = min(count,up-i+1)
            break
        elif down-1 >=2 and checkPrime(down-1):
            count = min(count,down-i+1)
            break
        up += 1
        down -= 1
    kq = max(kq,count)
print(kq)