import math
def check_prime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True
test = int(input())
ds = list(map(int,input().split()))
nt = list()
for i in ds:
    if check_prime(i):
        nt.append(i)
nt.sort()
index = 0
for i in ds:
    if i in nt:
        print(nt[index],end = ' ')
        index += 1
    else:
        print(i,end = ' ')