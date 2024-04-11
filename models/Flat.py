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

    def __eq__(self, other):
        if isinstance(other, Flat):
            return (
                    self.id == other.id and
                    self.number == other.number and
                    self.address == other.address and
                    self.isOccupied == other.isOccupied and
                    self.tenantId == other.tenantId
            )
        return False