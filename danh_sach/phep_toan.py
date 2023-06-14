def tinh(a,m):
    global ok
    s = ''
    for i in a:
        try: 
            x = int(i)
            if x<0:
                s += '('+str(x)+')'
            else:
                s += str(x) 
        except:
            s += i 
    kq = eval(s)
    if kq==m:
        s += f'={m}'
        ok = False
        print(s)
def back(a,ds,n,m,j):
    if len(a)==2*n-1:
        tinh(a,m)
    else:
        for i in '+-*':
            back(a+[i,ds[j+1]],ds,n,m,j+1)
global ok
ok = True
n,m = map(int,input().split())
ds = list(map(int,input().split()))
back([ds[0]],ds,n,m,0)
if ok:
    print('IMPOSSIBLE')