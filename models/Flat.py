class Flat:
    def __init__(self, id:int, number:int, address:str):
        self.id=id
        self.number = number
        self.address = address
        self.isOccupied = False
        self.tenantId=0

    def __str__(self):
        return f'{self.id} - {self.number} -  {self.address} - {self.isOccupied} - {self.tenantId}'

    def __repr__(self):
        return self.__str__()