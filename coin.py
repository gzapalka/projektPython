#!/usr/bin/env python
# coding: utf-8

# In[1]:
from decimal import *

class Coin:
    """Klasa Coin używana do reprezentacji pieniędzy"""

    def __init__(self, value):
        self._value = round(value, 2)
    
    @property
    def get_value(self):
        return self._value
    
    def __lt__(self, other):
        if self.get_value() < other.get_value():
            return True
        return False
    
    
if __name__ == '__main__':
    pass
else:
    print('Coin imported succenfully')




