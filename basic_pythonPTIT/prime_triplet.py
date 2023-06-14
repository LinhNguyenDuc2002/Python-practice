import math
def checkPrime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True
test = int(input())
while test > 0:
    n = int(input())
    count = 0
    for i in range(3,n-5,2):
        if checkPrime(i) and checkPrime(i+2) and checkPrime(i+6):
            count += 1
        elif checkPrime(i) and checkPrime(i+4) and checkPrime(i+6):
            count += 1
    print(count)
    test -= 1