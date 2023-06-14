def GT(n):
    gt = 1
    for i in range(2,n+1):
        gt*=i
    return gt
for i in range(0,int(input())):
    n = int(input())  
    m = n
    sum = 0
    while(m>0):
        sum += GT(m%10)  
        m//=10
    if sum == n:
        print("Yes")
    else:
        print("No")