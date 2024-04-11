class House:
    def __init__(self, id:int, street:str, house_number:str):
        self.id=id
        self.street = street
        self.houseNumber = house_number
        self.flats=[]
    uk_id:int

    def __str__(self):
        return f'{self.id} - {self.street} -  {self.houseNumber} - {self.flats}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, House):
            return (
                    self.id == other.id and
                    self.street == other.street and
                    self.houseNumber == other.houseNumber and
                    self.flats == other.flats and
                    self.uk_id == other.uk_id
            )
        return False