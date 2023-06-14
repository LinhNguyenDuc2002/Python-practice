ds = list()
while True:
    try:
        s = input().lower()
        x = ''
        for i in s:
            if i=='.'or i=='?' or i=='!':
                x = x.strip()
                x+=i
                ds.append(x)
                x = ''
            else:
                x += i
        if len(x)>0:
            ds.append(x)
    except:
        break
for i in ds:
    i = i.strip()
    i = i.capitalize()
    while i.find("  ")>=0:
        i = i.replace("  "," ")
    if not (i.endswith('.') or i.endswith('!') or i.endswith('?')):
        i+='.'
    print(i)