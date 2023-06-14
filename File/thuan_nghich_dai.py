import collections
def check(n):
    if n == n[::-1]:
        return True
    return False
with open('File/VANBAN.in','r') as file:
    ds = list()
    for line in file:
        ds += line.split()
    a = collections.Counter(ds)
    kq = list()
    max = ''
    for i in ds:
        if check(i):
            if len(i)>len(max):
                max = i
                kq.clear()
                kq.append(i)
            elif len(i)==len(max):
                if i not in kq:
                    kq.append(i)
    for i in kq:
        print(i,a[i])