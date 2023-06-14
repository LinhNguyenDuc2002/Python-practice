t = int(input())
ds = list()
while t>0:
    ds.append(input())
    t-=1
index = 0
for i in range(len(ds)):
    if len(ds[i])==0:
        print(f'{ds[index]}: {i-index-1}')
        index = i+1
print(f'{ds[index]}: {len(ds)-1-index}')

