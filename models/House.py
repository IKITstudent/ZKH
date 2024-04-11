class House:
    def __init__(self, id:int, street:str, house_number:str):
        self.id=id
        self.street = street
        self.houseNumber = house_number
        self.flats=[]

    def __str__(self):
        return f'{self.id} - {self.street} -  {self.houseNumber} - {self.flats}'

    def __repr__(self):
        return self.__str__()