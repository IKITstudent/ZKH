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

    def __eq__(self, other):
        if isinstance(other, Service):
            return (
                    self.id == other.id and
                    self.name == other.name and
                    self.price == other.price and
                    self.demand_type_ids == other.demand_type_ids
            )
        return False

