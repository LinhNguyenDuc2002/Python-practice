dict1 =  {
    'a':1,
    'b':2,
    'c':2
}
dict2 = {
    'a':5,
    'b':2,
    'd':5
}
a = [dict1[i] for i in dict1]
a = sum(a)
print(a)
