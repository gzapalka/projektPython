#!/usr/bin/env python
# coding: utf-8

# In[2]:


from decimal import *

class Ticket:
    """Klasa reprezentująca bilety"""
    def __init__(self,price: float, text: str):
        """Tworzy obiekt typu Ticket"""
        self._price = Decimal(str(price))
        text = text.replace("\n"," ")
        index = text.index("-")
        self._text = text[:index]
    
    @property
    def get_price(self) -> Decimal:
        """Zwraca wartość biletu"""
        return self._price
    
    @property
    def get_ticket_description(self) -> str:
        """Zwraca opis biletu"""
        return self._text
    
    def __str__(self):
        return self._text
    
    def __repr__(self):
        return self._text

