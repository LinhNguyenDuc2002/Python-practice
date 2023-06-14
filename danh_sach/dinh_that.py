import collections
def Back(u,v,way,visit,canh):
    if u==v:
        for i in kq:
            if i not in way:
                kq.remove(i)
    else:
        for i in canh[u]:
            if visit[i]==0:
                visit[i]==1
                way.append(i)
                Back(i,v,way,visit,canh)
                way.remove(i)
                visit[i]==0

test = int(input())
while test > 0:
    n,m,u,v = map(int,input().split())
    visit = [0]*(n+1)
    way = []
    kq = list()
    canh = {}
    for i in range(1,n+1):
        canh[i] = []
        if i!=u and i!=v:
            kq.append(i)
    for i in range(m):
        a,b = map(int,input().split())
        canh[a].append(b)
    way.append(u)
    visit[u] = 1
    Back(u,v,way,visit,canh)
    print(len(kq))
    test -= 1