#CodePTIT PY02018
# n = int(input()) 
# a = list(map(int,input().split()))
# for i in range(min(a),max(a)+2):
#     if i not in a:
#         print(i)
#         break

#CodePTIT PYKT079
test = int(input())
while test > 0:
    n = int(input())
    ds = list(map(int,input().split()))
    count = 0
    for i in range(min(ds),max(ds)):
        if i not in ds:
            count += 1
    print(count)
    test -=1