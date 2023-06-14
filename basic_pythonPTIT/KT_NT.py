# #CodePTIT PY01058
# import math, itertools
# def checkPrime(s):
#     if s<2:
#         return False
#     for i in range(2,int(math.sqrt(s))+1):
#         if s%i==0:
#             return False
#     return True
# test = int(input())
# while test>0:
#     s = input()
#     s = s[len(s)-4:len(s)]
#     if checkPrime(int(s)):
#         print("YES")
#     else:
#         print("NO")
#     test -= 1
    
# CodePTIT PY02031
import math, itertools
def checkPrime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True
m,n = map(int,input().split())
ds = list()
for i in range(0,m):
    a = list(map(int,input().split()))
    ds.append(a)
for i in range(0,m):
    for j in range(0,n):
        if checkPrime(ds[i][j]):
            ds[i][j] = 1
        else:
            ds[i][j] = 0
for i in ds:
    for j in i:
        print(j, end = ' ')
    print()