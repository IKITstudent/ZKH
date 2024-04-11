import models.House
from models import Tenant, Flat


from repos import fake_repo as r
from services import services as s

user1 = Tenant.Tenant(id=1, name="Name_1", phone=78965214545)
user2 = Tenant.Tenant(id=2, name="Name_2", phone=78965214141)

house = models.House.House(id=1, street="streetStr", house_number="12")

rT=r.TenantRepository

rT.save_item(item=user1)
t=rT.get_item(1)
print(t)

flat1= Flat.Flat(id=1, number=1, address="stree 1")

rF=r.FlatRepository

rF.save_item(item=flat1)
f=rF.get_item(1)
print(f)

a=s.AddUserToHouse(user1, house)
print(a)