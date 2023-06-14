#CodePTIT PY02032
s = input()
i,j = 0,2
ds = list()
while j<=len(s):
    if int(s[i:j]) not in ds:
        ds.append(int(s[i:j]))
    i = j
    j += 2
print(*ds)

#CodePTIT PY02034
# s = input()
# i,j = 0,2
# ds = dict()
# while j<=len(s):
#     a = s[i:j]
#     ds.update([(a,ds.get(a,0)+1)])
#     i = j
#     j += 2
# for i in ds:
#     print(i,ds.get(i))

#CodePTIT PY02035
# import collections
# s = input()
# k = int(input())
# i,j = 0,2
# ds = list()
# while j<=len(s):
#     ds.append(int(s[i:j]))
#     i = j
#     j += 2
# ds.sort()
# ds = collections.Counter(ds)
# check = True
# for i in ds:
#     if ds.get(i)>=k:
#         print(i,ds.get(i))
#         check = False
# if check:
#     print("NOT FOUND")