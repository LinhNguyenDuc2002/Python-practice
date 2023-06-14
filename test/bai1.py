import math
test = int(input())
t = 1
while t<=test:
    n = int(input())
    a = int((3+math.sqrt(5)))
    a **=n
    a = str(a)
    while len(a)<3:
        a = '0' + a
    if t<test:
        print(f'Case #{t}: {a[len(a)-3:]} ')
    else:
        print(f'Case #{t}: {a[len(a)-3:]}')
    t += 1