import unittest
import models

class TestHouse(unittest.TestCase):
    def setUp(self):
        self.House=models.House(10,"street","number")
        self.Tenant=models.Tenant(10,"name",100)
        self.Demand=models.Demand(10, "text",10,10,10,10,1,5)
        self.Flat=models.Flat(10, 123, "street 1")


    def testAddUserSuccess(self):
        self.assertEqual(self.House.AddUserToHouse(self.House,self.Tenant),"OK")

    def testAddUserFail(self):
        self.Tenant1=models.Tenant(10,100,100)
        self.assertEqual(self.House.AddUserToHouse(self.House,self.Tenant1),ValueError)

    def testSendDemandSuccess(self):
        self.assertEqual(self.Tenant.SendDemand(self.Tenant,"text",10),"OK")

    def testSendDemandFail(self):
        self.assertEqual(self.Tenant.SendDemand(self.Tenant,10,10),ValueError)

    def testSetDemandStatusFail(self):
        self.assertEqual(self.Demand.ChangeDemandStatus(self,"3"),ValueError)

    def testSetDemandStatusSuccess(self):
        self.assertEqual(self.Demand.ChangeDemandStatus(self, 3), "OK")

    def testAddTenentToFlatSuccess(self):
        self.assertEqual(self.Flat.AddTenantToFlat(self, self.Tenant),"OK")

    def testAddTenentToFlatFail(self):
        self.assertEqual(self.Flat.AddTenantToFlat(self, ""), ValueError)