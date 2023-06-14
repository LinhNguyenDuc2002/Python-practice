test = int(input())
s = input()
list1 = list()
for i in range(0,test):
    list1.append(int(s.split()[i]))
list2 = list()
for i in list1:
    list2.append(i)
    while len(list2)>=2:
        a = list2.pop()
        b = list2.pop()
        if (a+b)%2!=0:
            list2.append(b)
            list2.append(a)
            break
print(len(list2))

