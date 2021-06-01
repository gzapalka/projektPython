#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
import handler
import exceptions
import app
import numpy as np
import coin as c
from decimal import *

class Test_Handler(unittest.TestCase):
    def setUp(self):
        self.app = handler.Handler()
        
#     def test_shouldRaiseNoChangeNeeded_whenPaidActualAmount(self) -> None:
#         self.app.credit = 5
#         self.assertRaises(exceptions.NoChangeNeeded, self.app.manage_change, ["0","0","0","1","0","0","0","0","0","0","0","0"], app.App())
        
    def test_shouldGiveCorrectChange_WhenPossible(self) -> None:
        self.app.credit = 5
        result = self.app.manage_change(["0","0","0","1","1","0","0","0","0","0","0","0"])
        expected = np.array([c.Coin(Decimal(2).quantize(Decimal('0.00')))])

        np.testing.assert_array_equal(result, expected)
        
    def test_shouldNotGiveChange_whenCreditEqualPayment(self) -> None:
        self.app.credit = 5
        result = self.app.manage_change(["0","0","0","1","0","0","0","0","0","0","0","0"])
        expected = np.array([])

        np.testing.assert_array_equal(result, expected)
        
    def test_shouldReturnAddedCoin_whenCannotChange(self) -> None:
        self.app.credit = 6
        result = self.app.manage_change(["0","0","0","1","1","0","0","0","0","1","1","0"])
        expected = np.array([c.Coin(Decimal(5).quantize(Decimal('0.00'))),c.Coin(Decimal(2).quantize(Decimal('0.00'))),c.Coin(Decimal(0.05).quantize(Decimal('0.00'))),c.Coin(Decimal(0.02).quantize(Decimal('0.00')))])
        
        np.testing.assert_array_equal(result[1], expected)
        
    def test_shouldCalculateAmountToPay_Correctly(self)->None:
        self.app.credit = 1
        result = self.app.manage_change(["0","0","0","0","0","0","0","0","0","0","0","100"])
        expected = np.array([])

        np.testing.assert_array_equal(result, expected)
        
        
    def test_shouldCalculateCreditCorrectly(self)->None:
        fun1 = self.app.create_add_ticket(3, "reduced-")
        fun2 = self.app.create_add_ticket(5, "normal-")
        fun1()
        fun2()
        self.assertEqual(self.app.get_credit, 8)
        
    def test_coinsShouldNotDisappearAfterAddTicket(self) -> None:
        fun1 = self.app.create_add_ticket(3, "reduced-")
        fun1()
        self.app.insert_coins(["0","0","0","0","1","1","0","0","0","0","0","0"])
        fun1()
        result = self.app.manage_change(["0","0","0","0","1","1","0","0","0","0","0","0"])
        expected = np.array([])

        np.testing.assert_array_equal(result, expected)
        
    def test_shouldRaiseInvalidArgument_whenCoinAmountFloatOrNegative(self) -> None:
 
        self.assertRaises(exceptions.InvalidArgument, self.app.insert_coins, ["0","0","0","0","0","-1","0","0","0","0","0","0"])
        self.assertRaises(exceptions.InvalidArgument, self.app.insert_coins, ["0","0","0","0","0","1.1","0","0","0","0","0","0"])
        
if __name__ == '__main__':
    unittest.main()
else:
    print("Test_Handler imported succesfully")


# In[ ]:




