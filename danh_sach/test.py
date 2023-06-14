# def sum(ds,a,b):
#     x = 0
#     for i in range(a,b):
#         x += ds[i]
#     return x
# ds = list(map(int,input().split()))
# min = max(ds)
# start = -1
# end = -1
# for i in range(0,len(ds)):
#     for j in range(i+1,len(ds)):
#         a = sum(ds,i,j)
#         if a<min:
#             min = a
#             start = i
#             end = j
# if start != -1 and end != -1:
#     for i in range(start, end):
#         print(ds[i], end = ' ')

ds1 = list(map(int,input().split()))
ds2 = list(map(int,input().split()))
ds1.sort()
ds2.sort()

myset = set()
for i in ds1:
    myset.add(i)
for i in ds2:
    myset.add(i)
print("Hop 2 day: ", end ='')
for i in myset:
    print(i,end = ' ')
i = 0
j = 0
print("\nGiao 2 day: ", end ='')
while i<len(ds1)and j<len(ds2):
    if ds1[i]==ds2[j]:
        print(ds1[i],end = ' ')
        i += 1
        j += 1
    elif ds1[i]<ds2[j]:
        i += 1
    else:
        j += 1