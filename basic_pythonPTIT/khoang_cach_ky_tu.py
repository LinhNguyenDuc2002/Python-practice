test = int(input())
while test>0:
    s = input()
    i = 1
    j = len(s)-1
    check = True
    while i<len(s) and j>0:
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(s[j])-ord(s[j-1])):
            check = False
            break
        i += 1
        j -= 1
    if check:
        print("YES")
    else:
        print("NO")
    test -= 1