from decimal import Decimal, ROUND_HALF_UP
test = int(input())
while test>0:
    s = int(input())
    i = 1
    q = 10
    while s>q:
        r = '1E'+str(i)
        s = int(Decimal(s).quantize(Decimal(r),ROUND_HALF_UP))
        q*=10
        i+=1
    print(s)
    test-=1