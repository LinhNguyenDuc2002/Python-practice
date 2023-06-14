def dfs(u,n,a,vs):
    vs[u]=1
    for v in range(1,n+1):
        if vs[v]==0 and a[u][v]==1:
            dfs(v,n,a,vs)
n,m,k = map(int,input().split())
a = [[0] * (n+1) for _ in range(n+1)] # '_': chỉ ra ko quan tâm giá trị
vs = [0]*(n+1)
for i in range(0,m):
    x,y = map(int,input().split())
    a[x][y]=1
    a[y][x]=1
dfs(k,n,a,vs)
for i in range(1,n+1):
    if vs[i]==0:
        print(i)