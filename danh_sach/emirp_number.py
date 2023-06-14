import math
def checkPrime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s)+1)):
        if s%i==0:
            return False
    return True
test = int(input())
while test > 0:
    n = int(input())
    ds = [str(i) for i in range(11,n,2) if checkPrime(i)]
    for i in ds:
        x = i[::-1]
        if int(x)<n and i!=x and checkPrime(int(x)):
            print(i,x,sep = ' ',end = ' ')
            if x in ds:
                ds.remove(x)
    print()
    test -= 1