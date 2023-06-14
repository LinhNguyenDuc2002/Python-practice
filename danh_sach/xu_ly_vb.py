s = ''
while True:
    try:
        a = input()
        s += a + " "
    except EOFError:
        break
s = s.lower()
while s.find("  ")>=0:
    s = s.replace("  "," ")
index = 0
for i in range(len(s)):
    if s[i]=='.' or s[i]=='?' or s[i]=='!':
        a = s[index:i]
        a = a.strip()
        print(a.capitalize())
        index = i+1
a = s[index:]
if len(a)>0:
    print(a.strip().capitalize())