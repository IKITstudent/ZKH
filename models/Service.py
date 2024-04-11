class Service:
    def __init__(self, id:int,name:int, price:float, demand_type_ids:int):
        self.id=id
        self.name=name
        self.price=price
        self.demand_type_ids=demand_type_ids

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.price} - {self.demand_type_ids}'

    def __repr__(self):
        return self.__str__()