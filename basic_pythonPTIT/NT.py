# import math
# def checkPrime(a):
#     if a<2: return False
#     for i in range(2,int(math.sqrt(a))+1,1):
#         if a%i==0:
#             return False
#     return True
# test = int(input())
# while test>0:
#     n = int(input())
#     count = 0
#     for i in range(1,n,1):
#         if math.gcd(n,i)==1:
#             count += 1
#     print("YES") if checkPrime(count) else print("NO")
#     test -= 1

import math
def checkPrime(a):
    if a<2: return False
    for i in range(2,int(math.sqrt(a))+1,1):
        if a%i==0:
            return False
    return True
test = int(input())
while test>0:
    a,b = map(int,input().split())
    c = math.gcd(a,b)
    sum = 0
    for i in str(c):
        sum += int(i)
    if checkPrime(sum):
        print("YES")
    else:
        print("NO")
    test -= 1