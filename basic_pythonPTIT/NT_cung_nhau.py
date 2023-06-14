# #CodePTIT PY01030
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# s = input()
# n = int(s.split()[0])
# k = int(s.split()[1])
# mylist = []
# for i in range(10**(k-1),10**k):
#     if n%i!=0 and gcd(n,i)==1:
#         mylist.append(i)
# i = 0
# while i<len(mylist):
#     if i%10==0:
#         print()
#     print(f'{mylist[i]} ',end = '')
#     i += 1

#CodePTIT PY02019
import math
n = int(input())
ds = list(map(int,input().split()))
ds.sort()
for i in range(0,len(ds)):
    for j in range(i+1,len(ds)):
        if math.gcd(ds[i],ds[j])==1:
            print(ds[i],ds[j])
