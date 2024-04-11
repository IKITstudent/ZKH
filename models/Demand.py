class Demand:
    def __init__(self, id:int, text:str,house_id:int,flat_id:int, tenant_id:int, UK_id:int, demand_type_id):
        self.id=id
        self.text = text
        self.house_id=house_id
        self.flat_id=flat_id
        self.tenant_id=tenant_id
        self.UK_id = UK_id
        self.demand_type_id=demand_type_id

    def __str__(self):
        return f'{self.id} - {self.text} -  {self.house_id} - {self.flat_id} - {self.tenant_id} - {self.UK_id} - {self.demand_type_id}'

    def __repr__(self):
        return self.__str__()