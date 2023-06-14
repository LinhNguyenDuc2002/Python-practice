import math
def check_prime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True
n,x = map(int,input().split())
ds = list()
ds.append(2)
i = 3
while True:
    if len(ds)>n:
        break
    if check_prime(i):
        ds.append(i)
    i += 2
for i in ds:
    print(x, end = ' ')
    x += i
