def check(k):
    for i in s:
        if int(i/k)==int(i/(k+1)):
            return 0
    return 1
n = int(input())
s = list(map(int,input().split()))
m = min(s)
k = 0
sum = 0
for i in range(m,0,-1):
    if check(i):
        break
for j in range(n):
    sum += int(s[j]/(i+1))+1
print(sum)