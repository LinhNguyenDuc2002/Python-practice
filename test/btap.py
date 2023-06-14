# ds1 = list(map(int,input().split()))
# ds2 = list(map(int,input().split()))
# x = int(input())
# ds1.sort()
# ds2.sort()
# i = 0
# j = len(ds2)-1
# while i<len(ds1) and j>=0:
#     if ds1[i]+ds2[j]==x:
#         print(ds1[i],ds2[j])
#         i += 1
#         j -= 1
#     elif ds1[i]+ds2[j]<x:
#         i += 1
#     else:
#         j -= 1

n = int(input())
ds = list(input().split())
kq = ""
check = True
for i in ds[0]:
    kq += i
    for j in range(len(ds)):
        if not ds[j].startswith(kq):
            check = False
            break
    if check ==False:
        break
print(kq[0:len(kq)-1+])
    