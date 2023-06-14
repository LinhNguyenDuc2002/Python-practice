class Subject:
    def __init__(self,id,name,ht) -> None:
        self.id = id
        self.name = name
        self.ht = ht
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + self.ht
test = int(input())
ds = list()
while test > 0:
    a = Subject(input(),input(),input())
    ds.append(a)
    test -= 1
ds.sort(key=lambda x : x.id)
for i in ds:
    print(i)