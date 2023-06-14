#CodePTIT PY01016
test = int(input())
while test>0:
    s = input()
    mylist = []
    myvalue = []
    for i in range(0,len(s)):
        if i%2==0:
            mylist.append(s[i])
        else:
            myvalue.append(int(s[i]))
    for i in range(0,len(mylist)):
        print(mylist[i]*myvalue[i],end = '')
    print()
    test -= 1