#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Coin:

    def __init__(self, value, currency):
        if value in {0.01,0.02, 0.05, 0.1,0.2,0.5,1,2,5,10,20,50}:
            self._value = value
        else:
            self._value = 0
        if currency in {'PLN', 'EUR', 'GP'}:
            self._currency = currency
        else:
            self._currency = 'PLN'
    
    def get_value(self):
        return self._value
    
    def get_currency(self):
        return self._currency
    
    def __lt__(self, other):
        if self.get_value() < other.get_value():
            return True
        return False
    
    def __add__(self, other):
        return self.get_value() + other.get_value()
    
    def __add__(self, decimal):
        return self.get_value() + decimal
    
    def __int__(self):
        return self.get_value()
    
    def __str__(self):
        return "{}, {}".format(self._value, self._currency)
    def __repr__(self):
        return "{}, {}".format(self._value, self._currency)
    
if __name__ == '__main__':
    pass
else:
    print('Coin imported succenfully')


# In[ ]:




