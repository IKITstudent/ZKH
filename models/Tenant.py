class Tenant:
    def __init__(self, id:int, name:str, phone:int):
        self.id=id
        self.name = name
        self.phone = phone

    FlatNumber:int
    HouseAddress:str

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.phone}'

    def __repr__(self):
        return self.__str__()