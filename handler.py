#!/usr/bin/env python
# coding: utf-8

# In[1]:


import coin as c
import numpy as np
import payment_managment as pm
from decimal import *
from ticket import *
import exceptions
from typing import Callable


# In[34]:


class Handler(pm.Payment_Management):
    """Klasa obsługująca logikę działania automatu biletowego"""
    
    def __init__(self) -> None:
        """Tworzy handler do obsługi automatu biletowego"""
        super().__init__()
#         gui.GUI(self)
        self.available_tickets = ["Normalny\n20min-3zł","Normalny\n40min-4zł","Normalny\n60min-5zł","Ulgowy\n20min-2zł","Ulgowy\n40min-3zł","Ulgowy\n60min-4zł"]
        ticket_values = [3,4,5,2,3,4]
        self.ticket_values= [Decimal(ticket_values[i]).quantize(Decimal('0.00')) for i in range(len(ticket_values))]
        self.bought_ticket = []
        
    def create_add_ticket(self, value: float, description: str) -> Callable:
        """Zwraca funkcję naliczającą opłatę za konkretny bilet"""
        ticket = Ticket(value, description)
        def add_ticket() -> None:
            """Nalicza opłatę za bilet"""
            self.credit += ticket.get_price
            self.bought_ticket.append(ticket)
        return add_ticket
    
    def check_data(self, entry: list)-> bool:
        for e in entry:
            if not e.isnumeric():
                if e == "":
                    e = "0"
                else:
                    return False
        return True
    
    def resign(self) -> None:
        """Funckja resetująca"""
        self.credit = 0
        self.payment = 0
        self.bought_ticket = []
        
    def insert_coins(self, entry: list) -> list:
        """Dołącza wrzucone monety do zbioru"""
        added = np.array([])
        for e in range(len(entry)): 
            for i in range((int)(entry[e])):
                self.add_coin(self.expectedValue[e])
                added = np.append(added, c.Coin(self.expectedValue[e]))
        return added
                
    def manage_change(self, entry: list, gui) -> list:
        """Zwraca resztę jeżeli jest potrzebna lub rzuca wyjątek jeżeli to niemożliwe"""
        added = self.insert_coins(entry)
        if self.get_amount_to_pay < 0:
            self.resign()
            raise exceptions.NotEnoughMoney(gui.window)

        if self.get_amount_to_pay == 0:
            return []
            
        result = self.change(self.get_amount_to_pay)

        if type(result) == type(False):  
            for coin in added:
                self.return_coin(coin)
            raise exceptions.CannotChange(gui.window, added)
        else:
            return result
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




