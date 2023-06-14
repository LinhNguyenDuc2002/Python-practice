#CodePTIT PY01014
s = input()
mylist = s.split()
a = int(mylist[0])
k = int(mylist[1])
n = int(mylist[2])
check = False
i = 1
while k*i<=n:
    if (k*i-a)>0:
        print(k*i-a, end = ' ')
        check = True
    i += 1
if not check:
    print(-1)