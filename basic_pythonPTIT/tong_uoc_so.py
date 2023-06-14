import math
sum = 0
mydict = {}
mylist = list()
ngto = []
def checkPrime(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s)+1)):
        if s%i==0:
            return False
    return True
def cal(s):
    for j in ngto:
        if i%j==0:
            return mydict[j] + mydict[i//j]
test = int(input())
while test>0:
    s = int(input())
    mylist.append(s) 
    test -= 1
for i in range(2,max(mylist)+1):
    if i not in mydict:
        if checkPrime(i):
            mydict[i] = i
            ngto.append(i)
            mydict[i*i] = i+i
        else:
            mydi
            mydict[i] = cal(i)
    if i in mylist:
        sum += mydict[i]
print(mydict)
print(sum)