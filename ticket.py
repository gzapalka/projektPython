#!/usr/bin/env python
# coding: utf-8

# In[2]:


from decimal import *

class Ticket:
    """Klasa reprezentująca bilety"""
    def __init__(self,price: float):
        """Tworzy obiekt typu Ticket"""
        self._price = Decimal(str(price))
    
    @property
    def get_price(self) -> Decimal:
        """Zwraca wartość biletu"""
        return self._price

