with open('DATA.in','r') as file:
    ds = list()
    for line in file:
        a = line.split()
        for i in a:
            if len(i)<10:
                try:
                    s = int(i)
                except:
                    ds.append(i)
            else:
                ds.append(i)
    ds.sort()
    print(*ds)