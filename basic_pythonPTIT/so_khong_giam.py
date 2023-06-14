#CodePTIT PY01015
def check(s):
    for i in range(0,len(s)-1):
        if int(s[i])>int(s[i+1]):
            return False
    return True
test = int(input())
while test>0:
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    test -= 1
