#CodePTIT PY0205
m,n = map(int,input().split())
ds = list()
mmax,mmin = -1,10**8
for i in range(m):
    a = list(map(int,input().split()))
    ds.append(a)
    if max(a)>mmax:
        mmax = max(a)
    if min(a)<mmin:
        mmin = min(a)
check = True
for i in range(m):
    for j in range(n):
        if ds[i][j] == (mmax-mmin):
            if check:
                print(mmax-mmin)
            print(f'Vi tri [{i}][{j}]')
            check = False
if check:
    print("NOT FOUND")
