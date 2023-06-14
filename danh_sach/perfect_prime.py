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
    if checkPrime(n):
        sum = 0
        check = True
        for i in str(n):
            sum += int(i)
            if i!='2' and i!='3' and i!='5' and i!='7':
                check = False
                break
        if check:
            if checkPrime(int(str(n)[::-1])) and checkPrime(sum):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
    test -= 1