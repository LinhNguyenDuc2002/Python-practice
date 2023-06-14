test = int(input())
while test > 0:
    ds = list(input().split('.'))
    if len(ds)!=4:
        print("NO")
    else:
        check = True
        for i in ds:
            try:
                if int(i)<0 or int(i)>255:
                    check = False
                    break
            except:
                check = False
                break
        if check:
            print("YES")
        else:
            print("NO")
    test -= 1