import abc
from abc import ABC, abstractmethod
from models import *

class AbstractRepository(ABC):
    @abstractmethod
    def save_item(self, item):
        pass
    @abstractmethod
    def get_item(self, index):
        pass
class TenantRepository(AbstractRepository):
    __storage={}
    @staticmethod
    def save_item(item:Tenant):
        TenantRepository.__storage[item.id]=item
        return item

    @staticmethod
    def get_item(index:int):
        return TenantRepository.__storage.get(index)

class FlatRepository(AbstractRepository):
    __storage={}

    def save_item(item:Flat):
        FlatRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return FlatRepository.__storage.get(index)



class HouseRepository(AbstractRepository):
    __storage={}

    def save_item(item:House):
        HouseRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return HouseRepository.__storage.get(index)

class DemandRepository(AbstractRepository):
    __storage={}

    def save_item(item:Demand):
        DemandRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return DemandRepository.__storage.get(index)

class UKRepository(AbstractRepository):
    __storage={}

    def save_item(item:UK):
        UKRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return UKRepository.__storage.get(index)

class ServiceRepository(AbstractRepository):
    __storage={}

    def save_item(item:Service):
        ServiceRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return ServiceRepository.__storage.get(index)

class BillRepository(AbstractRepository):
    __storage={}

    def save_item(item:Bill):
        BillRepository.__storage[item.id]=item
        return item
    def get_item(index:int):
        return BillRepository.__storage.get(index)

