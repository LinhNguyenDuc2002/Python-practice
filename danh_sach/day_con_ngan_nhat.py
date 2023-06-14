import math
test = int(input())
while test > 0:
    n,k = map(int,input().split())
    ds = list(map(int,input().split()))
    if k in ds:
        print("1")
    else:
        for i in range(0,len(ds)):
            if ds[i]%k==0:
                ds[i]//=k
            else:
                ds[i]=-1
        check = False
        for i in range(2,len(ds)):
            j = 0
            while j<len(ds):
                if -1 not in ds[j:j+i]:
                    if math.gcd(ds[j:j+i])==k:
                        check = True
                        print(i)
                        break
                    else:
                        j += 1
                else:
                    j = ds.index
                
            if check==True:
                break
        if check==False:
            print(-1)
    test -= 1

6 9 7 10 12 24 36 27
