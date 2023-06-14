test = int(input())
ds = dict()
while test > 0:
    s = input().split()
    a = 0
    if s[3] == 'IN':
        if s[1] == 'Xe_con':
            if s[2] == '5':
                a = 10000
            else:
                a = 15000
        elif s[1] == 'Xe_tai':
            a = 20000
        else:
            if s[2] == '29':
                a = 50000
            else:
                a = 70000
    ds.update([(s[4],ds.get(s[4],0)+a)])
    test -= 1
for i in ds:
    print(f'{i}: {ds[i]}')
