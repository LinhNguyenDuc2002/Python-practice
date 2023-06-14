import datetime
class CaThi:
    def __init__(self,id,date,hour,idroom) -> None:
        self.id = "C"+'{:03d}'.format(id)
        self.date = date
        self.hour = hour
        # self.date = datetime.datetime.strptime(date,"%d/%m/%Y")
        # self.hour = datetime.datetime.strptime(hour,"%H:%M")
        self.idroom = idroom
    def __str__(self) -> str:
        return self.date + " " + self.hour + " " + self.idroom
        # return str(datetime.datetime.strftime(self.date,"%d/%m/%Y")) + " " + str(datetime.datetime.strftime(self.hour,"%H:%M")) + " " + self.idroom
