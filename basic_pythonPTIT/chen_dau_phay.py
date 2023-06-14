#CodePTIT PY01025
s = input()
kq = ''
i = len(s)
while i>=3:
    kq = ',' + s[i-3:i] + kq
    i -= 3
if i>0:
    kq = s[0:i] + kq
else:
    kq = kq[1:len(kq)]
print(kq)