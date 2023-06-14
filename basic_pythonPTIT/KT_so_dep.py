#CodePTIT PY01039
def check(s):
    my_set = set()
    for i in range(0,len(s)):
        if i<len(s)-1 and s[i]==s[i+1]:
            return False
        my_set.add(s[i])
    if len(my_set)==2:
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
