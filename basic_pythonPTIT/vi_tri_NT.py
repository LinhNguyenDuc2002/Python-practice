#CodePTIT PY01062
import math
def checkPrime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True
def check(s):
    mytuple = ('2','3','5','7')
    for i in range(0,len(s)):
        if checkPrime(i) and s[i] not in mytuple:
            return False
        elif not checkPrime(i) and s[i] in mytuple:
            return False
    return True
test = int(input())
while test>0:
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    test -= 1