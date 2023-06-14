test = int(input())
while test > 0:
    s = input()
    i = 100
    try:
        while s[i].isalnum():
            i -= 1
        print(s[:i])
    except:
        print(s)
    test -= 1