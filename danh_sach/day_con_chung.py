test = int(input())
while test > 0:
    a,b,c = map(int,input().split())
    ds1 = list(map(int,input().split()))
    ds2 = list(map(int,input().split()))
    ds3 = list(map(int,input().split()))
    x,y,z = 0,0,0
    check = False
    while x<len(ds1) and y<len(ds2) and z<len(ds3):
        if ds1[x] == ds2[y] == ds3[z]:
            print(ds1[x],end = ' ')
            check = True
            x += 1
            y += 1
            z += 1
        else:
            if ds1[x]<ds2[y]:
                x += 1
            elif ds2[y]<ds3[z]:
                y += 1
            elif ds3[z]<ds1[x]:
                z += 1
    if check:
        print()
    else:
        print("NO")
    test -= 1
