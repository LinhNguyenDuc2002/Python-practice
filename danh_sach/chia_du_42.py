test = 10
ds = list()
while len(ds)<10:
    a = list(map(int,input().split()))
    ds += a
kq =list()
for i in ds:
    if (i%42) not in kq:
        kq.append(i%42)
print(len(kq))
    