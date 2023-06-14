test = int(input())
while test>0:
    s = input()
    if len(s)%2==0:
        m = s[0:len(s)//2]
    else:
        m = s[0:len(s)//2+1]
    for i in range(0,int(m),2):
        a = str(i)+str(i)[::-1]
        if not('1' in a or '3' in a or '5' in a or '7' in a \
            or '9' in a):
            if int(a)<int(s) and int(a)>0:
                print(a, end = ' ')
            elif int(a)>=int(s):
                break
    print()
    test -= 1