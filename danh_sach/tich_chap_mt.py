# def tich(ds,a,i,j):
#     sum = 0
#     for x in range(i,i+3):
#         for y in range(j,j+3):
#             sum += ds[x][y]*a[x-i][y-j]
#     return sum
# test = int(input())
# while test > 0:
#     n,m = map(int,input().split())
#     ds = list()
#     for i in range(n):
#         x = list(map(int,input().split()))
#         ds.append(x)
#     a = list()
#     for i in range(3):
#         x = list(map(int,input().split()))
#         a.append(x)
#     sum = 0
#     for i in range(n-3+1):
#         for j in range(m-3+1):
#             sum+=tich(ds,a,i,j)
#     print(sum)
#     test -= 1

test = int(input())
while test > 0:
    n,m,l = map(int,input().split())
    a = list()
    a.append([0]*(m+1))
    for i in range(1,n+1):
        a.append(([0] + [int(x) for x in input().split()]))
    for i in range(1,n+1):
        for j in range(1,m+1):
            a[i][j] += a[i][j-1] + a[i-1][j] - a[i-1][j-1]
    for i in range(1,n-l+2):
        for j in range(1,m-l+2):
            k = a[i+l-1][j+l-1] - a[i-1][j+l-1] - a[i+l-1][j-1] + a[i-1][j-1]
            k = k//(l*l)
            print(k,end=' ')
        print()
    test -= 1