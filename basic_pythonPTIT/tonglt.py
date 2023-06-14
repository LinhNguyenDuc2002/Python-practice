import math, sys
test = int(input())
for line in sys.stdin:
    n = int(line)
    count = 0
    x = int(math.sqrt(8*n))
    if x%2==0: x += 1
    else: x += 2
    while True:
        a = math.sqrt(x*x-8*n)
        i = (int(a) + 1)//2
        if float(a).is_integer():
            delta = (2*i-1)**2+8*n
            kq = (int(math.sqrt(delta))-1)//2
            print("x=",x)
            if i>0 and i<=n//2:
                count += 1
                print('kq=',kq)
                x = int(math.sqrt((kq*2-1)**2+8*n))
                if x%2==0: x += 1
            else:
                break
        else:
            if i>n//2:
                break
            x += 2
    print(count)
    test -= 1
    if test==0: break