#PY01019
# test = int(input())
# while test>0:
#     s = input()
#     i = 1
#     j = len(s)-1
#     check = True
#     while i<len(s) and j>0:
#         if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(s[j])-ord(s[j-1])):
#             check = False
#             break
#         i += 1
#         j -= 1
#     if check:
#         print("YES")
#     else:
#         print("NO")
#     test -= 1

#PY01024
# def check(s):
#     sum = int(s[0])
#     for i in range(1,len(s)):
#         sum += int(s[i])
#         if abs(int(s[i])-int(s[i-1]))!=2:
#             return False
#     if sum%10==0:
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

#PY01029
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# test = int(input())        
# while test>0:
#     s = input()
#     if gcd(int(s),int(s[::-1]))==1:
#         print("YES")
#     else:
#         print("NO")
#     test -= 1

#PY01036
# test = int(input())
# while test>0:
#     n = int(input())
#     sum = 0
#     if n%2==0:
#         x = 2
#     else:
#         x = 1
#     for i in range(x,n+1,2):
#         sum += 1/i
#     print('%.6f' %(sum))
#     test -= 1

#PY01038
# test = int(input())
# while test>0:
#     s = input()
#     check = False
#     i = 0
#     sum = int(s)
#     while i<1000:
#         if sum%7==0:
#             check = True
#             break
#         sum = sum + int(str(sum)[::-1])     
#     if check:
#         print(sum)
#     else:
#         print(-1)
#     test -= 1

#PY01039
# def check(s):
#     my_set = set()
#     for i in range(0,len(s)):
#         if i<len(s)-1 and s[i]==s[i+1]:
#             return False
#         my_set.add(s[i])
#     if len(my_set)==2:
#         return True
#     else:
#         return False
# test = int(input())
# while test>0:
#     s = input()
#     if check(s):
#         print("YES")
#     else:
#         print("NO")
#     test -= 1

#PY01043
# def check(s):
#     for i in s:
#         if int(i)%2!=0:
#             return False
#     return True
# test = int(input())
# while test>0:
#     s = input()
#     a = int(s)
#     if len(s)%2==0:
#         s = s[0:len(s)//2]
#     else:
#         s = s[0:len(s)//2+1]
#     for i in range(2,int(s)):
#         r = str(i)+str(i)[::-1]
#         if int(r)<a and len(r)%2==0 and check(str(i)):
#             print(r, end = ' ')
#     print()
#     test -= 1

#PY01045
# s = input()
# print(len(s)-1)

#PY01049
# import math
# def checkPrime(s):
#     if s<2:
#         return False
#     for i in range(2,int(math.sqrt(s)+1)):
#         if s%i==0:
#             return False
#     return True
# def check(s):
#     count =0
#     for i in s:
#         if checkPrime(int(i)):
#             count += 1
#     if count > len(s) - count:
#         return True
# test = int(input())
# while test>0:
#     s = input()
#     if checkPrime(len(s)) and check(s):
#         print("YES")
#     else:
#         print("NO")
#     test -= 1

#PY01063
# test = int(input())
# while test>0:
#     s = input()
#     n = input()
#     print(s.count(n))
#     test -= 1