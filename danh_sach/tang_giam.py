test = int(input())
while test > 0:
    n = int(input())
    a = list()
    b = list()
    gt = [1]*n
    for i in range(n):
        s = input().split()
        a.append(float(s[0]))
        b.append(float(s[1]))
    kq = 1
    for i in range(n):
        for j in range(0,i):
            if a[j]<a[i] and b[j]>b[i]:
                gt[i] = max(gt[i],gt[j]+1)
        kq = max(kq,gt[i])
    print(kq)
    test -= 1
