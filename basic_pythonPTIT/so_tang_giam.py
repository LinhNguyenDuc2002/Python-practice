#CodePTIT PY01041
def check(s):
    if len(s)<3:
        return False
    for i in range(0,len(s)):
        if int(s[i])>int(s[i+1]):
            break
        elif int(s[i])==int(s[i+1]):
            return False
    if i<len(s)-1:
        for j in range(i,len(s)-1):
            if int(s[j])<= int(s[j+1]):
                return False
        return True
    else:
        return False
test = int(input())
while test>0:
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    test -= 1