import repos.fake_repo as fr


class Demand:
    def __init__(self, id:int, text:str,house_id:int,flat_id:int, tenant_id:int, UK_id:int, demand_type_id:int,demand_status_id:int):
        self.id=id
        self.text = text
        self.house_id=house_id
        self.flat_id=flat_id
        self.tenant_id=tenant_id
        self.UK_id = UK_id
        self.demand_type_id=demand_type_id
        self.demand_status_id=demand_status_id

    def __str__(self):
        return f'{self.id} - {self.text} -  {self.house_id} - {self.flat_id} - {self.tenant_id} - {self.UK_id} - {self.demand_type_id}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Demand):
            return (
                    self.id == other.id and
                    self.text == other.text and
                    self.house_id == other.house_id and
                    self.flat_id == other.flat_id and
                    self.tenant_id == other.tenant_id and
                    self.UK_id == other.UK_id and
                    self.demand_type_id == other.demand_type_id and
                    self.demand_status_id==other.demand_status_id
            )
        return False

    def ChangeDemandStatus(self, newStatusId: int):
        self.demand_status_id = newStatusId
        fr.DemandRepository.save_item(self)
        return "OK"