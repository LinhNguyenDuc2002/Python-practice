import math
def checkPrime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n = int(input())
ds = list(map(int,input().split()))
dsset = list()
sum_right= 0
for i in ds:
    if i not in dsset:
        dsset.append(i)
        sum_right += i
sum_left = 0
for i in range(len(dsset)):
    sum_left += dsset[i]
    sum_right -= dsset[i]
    if checkPrime(sum_left) and checkPrime(sum_right):
        print(i)
        break
if sum_right == 0:
    print("NOT FOUND")
