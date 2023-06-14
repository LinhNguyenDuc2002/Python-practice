#CodePTIT PY01017
# test = int(input())
# while test>0:
#     s = input()
#     count  = 0
#     char = s[0]
#     for i in s:
#         if i==char:
#             count += 1
#         else:
#             print(count, char, sep = '', end = '')
#             count = 1
#             char = i
#     if count>0:
#         print(count, char, sep = '')
#     test -= 1

#CodePTIT PY01018
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s = input()
    k = int(s.split()[0])
    if k==0:
        break
    m = s.split()[1]
    kq = ''
    for i in range(0,len(m)):
        j = p.find(m[i])
        kq += p[(j+k)%28]
    kq = kq[::-1]
    print(kq)
