#!/usr/bin/env python
# coding: utf-8

# In[1]:


import coin as c
import numpy as np
import payment_managment as pm
from decimal import *
from ticket import *
import exceptions
import gui


# In[34]:


class Ticket_Machine(pm.Payment_Management):
    """Klasa obsługująca logikę działania automatu biletowego"""
    def __init__(self):
        super().__init__()
#         gui.GUI(self)
        self.available_tickets = ["20min\n3zł","40min\n4zł","60min\n5zł","20min\n2zł","40min\n3zł","60min\n4zł"]
        ticket_values = [3,4,5,2,3,4]
        self.ticket_values= [Decimal(ticket_values[i]).quantize(Decimal('0.00')) for i in range(len(ticket_values))]
        
    def create_add_ticket(self, value: float):
        """Zwraca funckję naliczającą opłatę za konkretny bilet"""
        ticket = Ticket(value)
        def add_ticket() -> None:
            """Nalicza opłatę za bilet"""
            self.credit += ticket.get_price
        return add_ticket
    
    def resign(self) -> None:
        """Funckja resetująca"""
        self.credit = 0
        self.payment = 0
#         self.gui.update_credit_status()
#         self.gui.display_paymnet_layout = False
        
    def addCoinsToPM(self, entry):
        added = np.array(self.get_payment)
        for e in range(len(entry)): #numer wejścia
            for i in range((int)(entry[e])): #po danych
                self.add_coin(self.expectedValue[e])
                added = np.append(added, c.Coin(self.expectedValue[e]))
        return added
                
    def checkData(self, entry):
        for e in entry:
            if not e.isnumeric():
                if e == "":
                    e = "0"
                else:
                    return False
        return True
        
    def manage_change(self, entry, gui):
        print("Najpierw: "+ (str)(self.lista))
        added = self.addCoinsToPM(entry)
        print("Po dodaniu: "+ (str)(self.lista))
        if self.get_amount_to_pay < 0:
            self.resign()
            raise exceptions.NotEnoughMoney(gui.window)

        if self.get_amount_to_pay == 0:
            print("Nie wydawać: "+ (str)(self.lista))
            return []
            
        result = self.change(self.get_amount_to_pay)

        if type(result) == type(False):  
            for coin in added:
                self.return_coin(coin)
            raise exceptions.CannotChange(gui.window, added)
        else:
            print(result)
            print("Na koniec: "+ (str)(self.lista))
            return result
        
#         except Exception as exc:
#         return added

        
        
        


# In[35]:


# app = Ticket_Machine()
# app.credit = 6
# print(app.manageChange(["0","0","0","1","1","1","1","0","0","1","1","0"]))


# In[36]:


import unittest

class TestPM(unittest.TestCase):
    def setUp(self):
        self.app = Ticket_Machine()
        
    def test_shouldRaiseNoChangeNeeded_whenPaidActualAmount(self) -> None:
        self.app.credit = 5
        self.assertRaises(exceptions.NoChangeNeeded, self.app.manageChange, ["0","0","0","1","0","0","0","0","0","0","0","0"])
        
    def test_shouldGiveCorrectChange_WhenPossible(self) -> None:
        self.app.credit = 5
        result = self.app.manageChange(["0","0","0","1","1","0","0","0","0","0","0","0"])
        expected = np.array([c.Coin(Decimal(2).quantize(Decimal('0.00')))])

        np.testing.assert_array_equal(result, expected)

        
    def test_shouldReturnAddedCoin_whenCannotChange(self) -> None:
        self.app.credit = 6
        print(self.app.manageChange(["0","0","0","1","1","1","1","0","0","1","1","0"]))
        
if __name__ == '__main__':
    unittest.main()


# In[ ]:




