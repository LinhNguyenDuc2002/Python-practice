#CodePTIT PY01056
import math
def check(s):
    for i in range(0,len(s)):
        if i%2==0 and int(s[i])%2!=0:
            return False
        elif i%2!=0 and int(s[i])%2==0:
            return False
    return True
def checkPrime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True
test = int(input())
while test>0:
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if check(s) and checkPrime(sum):
        print("YES")
    else:
        print("NO")
    test -= 1