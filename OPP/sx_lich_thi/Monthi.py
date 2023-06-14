class MonThi:
    def __init__(self,id,name,test) -> None:
        self.id = id
        self.name = name
        self.test = test
    def __str__(self) -> str:
        return self.name