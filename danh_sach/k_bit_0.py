test = int(input())
while test>0:
    n,k=map(int,input().split())
    ds = bin(n)[2:]
    while ds[0]=='0':
        ds = ds[1:]
    print(ds)
    test -= 1