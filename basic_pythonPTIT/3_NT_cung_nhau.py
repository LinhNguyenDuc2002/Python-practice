def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
s = input()
a = int(s.split()[0])
b = int(s.split()[1])
my_list1 = []
my_list2 = []
for i in range(a,b):
    for j in range(i+1,b+1):
        if gcd(i,j)==1:
            my_list1.append((i,j))
            my_list2.append(i*j)
for i in range(0,len(my_list1)):
    for j in range(a+2,b+1):
        if j>my_list1[i][1] and gcd(my_list2[i],j)==1:
            print(f'({my_list1[i][0]}, {my_list1[i][1]}, {j})')
