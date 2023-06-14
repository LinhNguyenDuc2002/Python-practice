# from datetime import datetime
# import math
# class ThiSinh:
#     def __init__(self,name,date,mark1,mark2,mark3) -> None:
#         self.name = name
#         self.date = date
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
#     def __str__(self) -> str:
#         date = datetime.strptime(self.date, "%d/%m/%Y")#string->date
#         return self.name + " " + date.strftime("%d/%m/%Y") + " " + '{:.1f}'.format(self.mark1+self.mark2+self.mark3)#date->string
# ts = ThiSinh(input(),input(),float(input()),float(input()),float(input()))
# print(ts.__str__())

class TS:
    def __init__(self,name,dob,mark1,mark2,mark3) -> None:
        self.name = name
        self.dob = dob
        self.sum = mark1+mark2+mark3
    def __str__(self) -> str:
        return self.name +" " + self.dob + " " + "{:.1f}".format(self.sum)

name = input()
dob = input()
mark1 = float(input())
mark2 = float(input())
mark3 = float(input())
ts = TS(name,dob,mark1,mark2,mark3)
print(ts)

