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
        self.added_coins = np.array([])
        
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
        
    def insert_coins(self, entry: list, gui = None) -> list:
        """Dołącza wrzucone monety do zbioru"""
        if not self.check_data(entry):
            raise exceptions.InvalidArgument(gui)
            
        for e in range(len(entry)): 
            for i in range((int)(entry[e])):
                self.add_coin(self.expectedValue[e])
                self.added_coins = np.append(self.added_coins, c.Coin(self.expectedValue[e]))
        return self.added_coins
                
    def manage_change(self, entry: list, gui = None) -> list:
        """Zwraca resztę jeżeli jest potrzebna lub rzuca wyjątek jeżeli to niemożliwe"""
        added = self.insert_coins(entry, gui)
        if self.get_amount_to_pay < 0:
            self.resign()
            raise exceptions.NotEnoughMoney(gui.window)

        if self.get_amount_to_pay == 0:
            return []
            
        result = self.change(self.get_amount_to_pay)

        if type(result) == type(False):  
            for coin in added:
                self.return_coin(coin)
            return False, added
#             raise exceptions.CannotChange(gui.window, added)
        else:
            return result

# In[ ]:




