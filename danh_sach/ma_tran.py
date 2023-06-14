#CodePTIT PY02039
n = int(input())
matrix = list()
for i in range(0,n):
    ds = list(map(int,input().split()))
    matrix.append(ds)
k = int(input())
sum1 = 0
sum2 = 0
for i in range(0,n):
    for j in range(0,n):
        if j>i:
            sum1 += matrix[i][j]
        elif j<i:
            sum2 += matrix[i][j]
a = abs(sum1-sum2)
if a<=k:
    print(f"YES\n{a}")
else:
    print(f"NO\n{a}")

#CodePTIT PY02040
# n = int(input())
# matrix = list()
# for i in range(0,n):
#     ds = list(map(int,input().split()))
#     matrix.append(ds)
# k = int(input())
# sum1 = 0
# sum2 = 0
# for i in range(0,n):
#     for j in range(0,n):
#         if (j+i)<(n-1):
#             sum1 += matrix[i][j]
#         elif (j+i)>=n:
#             sum2 += matrix[i][j]
# a = abs(sum1-sum2)
# if a<=k:
#     print(f"YES\n{a}")
# else:
#     print(f"NO\n{a}")
