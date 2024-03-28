from enum import Enum

class Tenant:
    def __init__(self, id:int, name:str, phone:int):
        self.id=id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.phone}'

    def __repr__(self):
        return self.__str__()
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
class UK:
    def __init__(self, id:int,name:str,houses:[House]):
        self.id=id
        self.name=name
        self.houses=houses

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.houses}'
    def __repr__(self):
        return self.__str__()
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
class Bill:
    def __init__(self, id:int, pay:float, tenant_id:int, UK_id:int, description:str):
        self.id=id
        self.pay=pay
        self.tenant_id = tenant_id
        self.UK_id = UK_id
        self.description = description

    def __str__(self):
        return f'{self.id} - {self.pay} -  {self.tenant_id} - {self.UK_id} -  {self.description}'

    def __repr__(self):
        return self.__str__()