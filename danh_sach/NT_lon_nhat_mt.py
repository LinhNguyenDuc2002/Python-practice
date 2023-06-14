#CodePTIT PY02055
import math
def check_prime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True
m,n = map(int,input().split())
ds = list()
for i in range(m):
    a = list(map(int,input().split()))
    ds.append(a)
x = list()
y = list()
max = -1
for i in range(m):
    for j in range(n):
        if ds[i][j] == max:
            x.append(i)
            y.append(j)
        else:
            if check_prime(ds[i][j]) and ds[i][j] > max:
                max = ds[i][j]
                x.clear()
                y.clear()
                x.append(i)
                y.append(j)
if max == -1:
    print("NOT FOUND")
else:
    print(max)
    for i in range(len(x)):
        print(f'Vi tri [{x[i]}][{y[i]}]')
