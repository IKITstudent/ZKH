import models.Tenant, models.Service, models.House, models.UK, models.Bill, models.Flat, models.Demand
from repos.repository import AbstractRepository
#from models import Tenant,Flat, Bill, Demand, Service, UK,House

class TenantRepository(AbstractRepository):
    __storage={}
    @staticmethod
    def save_item(item:models.Tenant):
        TenantRepository.__storage[item.id]=item
        return item

    @staticmethod
    def get_item(index:int):
        return TenantRepository.__storage.get(index)

class FlatRepository(AbstractRepository):
    __storage={}

    def save_item(item:models.Flat):
        FlatRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return FlatRepository.__storage.get(index)



class HouseRepository(AbstractRepository):
    __storage={}

    def save_item(item:models.House):
        HouseRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return HouseRepository.__storage.get(index)

class DemandRepository(AbstractRepository):
    __storage={}

    def save_item(item:models.Demand):
        DemandRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return DemandRepository.__storage.get(index)

class UKRepository(AbstractRepository):
    __storage={}

    def save_item(item:models.UK):
        UKRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return UKRepository.__storage.get(index)

class ServiceRepository(AbstractRepository):
    __storage={}

    def save_item(item:models.Service):
        ServiceRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return ServiceRepository.__storage.get(index)

class BillRepository(AbstractRepository):
    __storage={}

    def save_item(item:models.Bill):
        BillRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return BillRepository.__storage.get(index)

