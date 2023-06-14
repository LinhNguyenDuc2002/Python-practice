class Team:
    def __init__(self,id,name,school) -> None:
        self.id = "Team"+"{:02d}".format(id)
        self.name = name
        self.school = school
    def __str__(self) -> str:
        return self.name + " " + self.school
class ThiSinh:
    def __init__(self,id,name,team) -> None:
        self.id = "C"+"{:03d}".format(id)
        self.name = name
        self.team = team
    def __str__(self) -> str:
        return self.id +" " + self.name +" " + self.team.__str__()

n = int(input())
dsTeam = dict()
for i in range(1,n+1):
    name = input()
    school = input()
    a = Team(i,name,school)
    dsTeam[a.id] = a
m = int(input())
dssv = list()
for i in range(1,m+1):
    name = input()
    idTeam = input()
    a = ThiSinh(i,name,dsTeam[idTeam])
    dssv.append(a)
dssv.sort(key=lambda x : x.name)
for i in dssv:
    print(i)