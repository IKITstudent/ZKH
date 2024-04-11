from dataclasses import dataclass
@dataclass(frozen=True)
class Bill:
        id:int
        pay:float
        tenant_id:int
        UK_id:int
        description:str
'''
    def __str__(self):
        return f'{self.id} - {self.pay} -  {self.tenant_id} - {self.UK_id} -  {self.description}'

    def __repr__(self):
        return self.__str__()
'''