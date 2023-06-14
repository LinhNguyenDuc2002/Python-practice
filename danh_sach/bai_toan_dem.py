n = int(input())
ds = list()
while n > 0:
    s = list(map(int,input().split()))
    ds += s
    n -= len(s)
kq = list()
for i in range(1,max(ds)):
    if i not in ds:
        kq.append(i)
if len(kq)==0:
    print("Excellent!")
else:
    for i in kq:
        print(i)