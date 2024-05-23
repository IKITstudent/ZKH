import  Demand
import House
import  UK
import repos.fake_repo as fr

class Tenant:
    def __init__(self, id:int, name:str, phone:int):
        self.id=id
        self.name = name
        self.phone = phone

    FlatNumber:int
    HouseAddress:str

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.phone}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Tenant):
            return (
                    self.id == other.id and
                    self.name == other.name and
                    self.phone == other.phone and
                    self.FlatNumber == other.FlatNumber and
                    self.HouseAddress == other.HouseAddress
            )
        return False

    def SendDemand(self, text: str, houseId: int):
        newDemand: Demand
        house: House
        uk: UK

        house = fr.HouseRepository.get_item(houseId)
        uk = fr.UKRepository.get_item(house.uk_id)

        newDemand(tenant_id=self.id, text=text, house_Id=houseId, uk_id=uk.id, demand_type_id=1)

        fr.DemandRepository.save_item(newDemand)

        return "OK"