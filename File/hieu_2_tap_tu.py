ds1 = set()
ds2 = set()
with open('File/DATA1.in','r') as my_file:
    a = list()
    for line in my_file:
        line = line.lower()
        a += line.split()
    for x in a: ds1.add(x)
    ds1 = list(ds1)
    ds1.sort()
with open('File/DATA2.in','r') as my_file:
    b = list()
    for line in my_file:
        line = line.lower()
        b += line.split()
    for x in b: ds2.add(x)
    ds2 = list(ds2)
    ds2.sort()
print(*[i for i in ds1 if i not in ds2], end=' ')
print()
print(*[i for i in ds2 if i not in ds1], end=' ')