s = input()
sum = 0
count = 0
while len(s)>1:
    for i in s:
        if i == '-':
            sum += ord('-') - ord('0')
        else:
            sum += int(i)
    s = str(sum)
    count += 1
    sum = 0
print(count)