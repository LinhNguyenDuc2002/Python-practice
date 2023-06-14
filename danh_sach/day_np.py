test = int(input())
s = input()
s = s.replace(" ",'')
count  = 0
count += s.count('01')
count += s.count('10')
print(count)