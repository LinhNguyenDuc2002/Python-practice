with open('File/CONTACT.in','r') as my_file:
    ds = set()
    for line in my_file:
        line = line.strip()
        ds.add(line.lower())
    ds = list(ds)
    ds.sort()
    for i in ds:
        print(i)