from models import Tenant,Demand,UK, House, Flat
import repos.fake_repo as fr

def AddUserToHouse(tenant: Tenant, house:House):
    tenant.HouseAddress=house.street+", "+house.houseNumber
    fr.TenantRepository.save_item(tenant)
    return "OK"

def SendDemand(tenant:Tenant,text:str, houseId:int):
    newDemand:Demand
    house:House
    uk:UK

    house=fr.HouseRepository.get_item(houseId)
    uk=fr.UKRepository.get_item(house.uk_id)

    newDemand(tenant_id=tenant.id,text=text,house_Id=houseId,uk_id=uk.id,demand_type_id=1)

    fr.DemandRepository.save_item(newDemand)

def AddTenantToFlat(flat:Flat, tenant:Tenant):
    tenant.FlatNumber=flat.number
    fr.TenantRepository.save_item(tenant)
    return "OK"

def ChangeDemandStatus(demand:Demand, newStatusId:int):
    demand.demand_status_id=newStatusId
    fr.DemandRepository.save_item(demand)
    return "OK"