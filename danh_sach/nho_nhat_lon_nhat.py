while True:
    n = int(input())
    if n==0:
        break
    ds = set()
    for i in range(n):
        ds.add(int(input()))
    if len(ds)==1:
        print("BANG NHAU")
    else:
        ds = list(ds)
        ds.sort()
        print(ds[0],ds[len(ds)-1])
    
