#PY01002
# s = str(input())
# i = s.find('=')
# s1 = s[0:i]
# s2 = s[i+1:len(s)]
# s1 = eval(s1)
# s2 = int(s2)
# # print(s1,s2)
# if s1==s2:
#     print("YES")
# else:
#     print("NO")

#PY01004
# from math import sqrt
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# def checkPrime(a):
#     if a<2: return False
#     for i in range(2,int(sqrt(a))+1,1):
#         if a%i==0:
#             return False
#     return True
# test = int(input())
# while test>0:
#     n = int(input())
#     count = 0
#     for i in range(1,n,1):
#         if gcd(n,i)==1:
#             count += 1
#     if checkPrime(count):
#         print("YES")
#     else:
#         print("NO")
#     test -= 1

#PY01005
# s = input()
# number4 = 0
# number7 = 0
# for i in s:
#     if i=='4': number4 += 1
#     elif i=='7': number7 += 1
# sum = number4+number7
# if sum==4 or sum==7: 
#     print("YES")
# else:
#     print("NO")

#PY01006
# def check(s):
#     for i in s:
#         if i!='4' and i!='7': return False
#     return True
# test = int(input())
# while test>0:
#     s = str(input())
#     if check(s)==True:
#         print("YES")
#     else:
#         print("NO")
#     test -= 1

#PY01008
# s = str(input())
# print(s.upper())

#PY01009
# s = input()
# upper = 0
# lower = 0
# for i in s:
#     if i.isupper():
#         upper += 1
#     else:
#         lower += 1
# if upper>lower:
#     print(s.upper())
# else:
#     print(s.lower())

#PY01010
# test = int(input())
# while test>0:
#     s = input()
#     s1 = s[0:2]
#     s2 = s[len(s)-2:len(s)]
#     if s1==s2:
#         print("YES")
#     else:
#         print("NO")
#     test -=1

#PY01013
# import math
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# def checkPrime(a):
#     if a<2: return False
#     for i in range(2,int(math.sqrt(a))+1,1):
#         if a%i==0:
#             return False
#     return True
# test = int(input())
# while test>0:
#     s = input()
#     a = int(s.split()[0])
#     b = int(s.split()[1])
#     c = gcd(a,b)
#     sum = 0
#     for i in str(c):
#         sum += int(i)
#     if checkPrime(sum):
#         print("YES")
#     else:
#         print("NO")
#     test -= 1

#PY01059
# test = int(input())
# while test>0:
#     s = input()
#     sum = 0
#     tich = 1
#     check = False
#     for i in range(0,len(s)):
#         if i%2==0:
#             sum += int(s[i])
#         else:
#             if s[i]!='0':
#                 check = True
#                 tich *= int(s[i])
#     if check:
#         print(sum,tich)
#     else:
#         print(sum,0)
#     test -= 1

#PY01062
# import math
# def checkPrime(s):
#     if s<2:
#         return False
#     for i in range(2,int(math.sqrt(s))+1):
#         if s%i==0:
#             return False
#     return True
# def check(s):
#     if not checkPrime(len(s)):
#         return False
#     count = 0
#     for i in s:
#         if i=='2' or i=='3' or i=='5' or i=='7':
#             count += 1
#     if count > len(s)-count:
#         return True
#     return False
# test = int(input())
# while test>0:
#     s = input()
#     if check(s):
#         print("YES")
#     else:
#         print("NO")
#     test -= 1
