import models.House as h

class UK:
    def __init__(self, id:int,name:str,houses:[h]):
        self.id=id
        self.name=name
        self.houses=houses

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.houses}'
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, UK):
            return (
                    self.id == other.id and
                    self.name == other.name and
                    self.houses == other.houses
            )
        return False