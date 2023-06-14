import collections
test = int(input())
t = 1
while t<=test:
    mydict1 = collections.Counter(input()[0::1])
    mydict2 = collections.Counter(input()[0::1])
    if mydict1==mydict2:
        print(f'Test {t}: YES')
    else:
        print(f'Test {t}: NO')
    t+=1

