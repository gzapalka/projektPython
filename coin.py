#!/usr/bin/env python
# coding: utf-8

# In[2]:


from decimal import *
import unittest

class Coin:
    """Klasa rezprezentująca monety"""
    def __init__(self, value: float):
        """Tworzy nowy obiekt typu Coin"""
        self._value = Decimal(round(value, 2))
        
    @property
    def get_value(self) -> Decimal:
        """Zwraca wartość monety"""
        return self._value
    
    def __lt__(self, other):
        """Umożliwia porównywanie dwóch obiektów typu Coin"""
        if self.get_value < other.get_value:
            return True
        return False
    
    def __str__(self):
        return (str)(self.get_value)
    
    def __repr__(self):
        return (str)(self.get_value)
    
    def __eq__(self, other):
        return self.get_value==other.get_value
    
if __name__ == '__main__':
    pass
else:
    print('Coin imported succenfully')


# In[ ]:




