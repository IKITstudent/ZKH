from models import Tenant,Flat
from repos import repository as r

user1= Tenant(id=1, name="Name_1", phone=78965214545)
user2= Tenant(id=2, name="Name_2", phone=78965214141)

rT=r.TenantRepository

rT.save_item(item=user1)
t=rT.get_item(1)
print(t)

flat1= Flat(id=1, number=1, address="stree 1")

rF=r.FlatRepository

rF.save_item(item=flat1)
f=rF.get_item(1)
print(f)
