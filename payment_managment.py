#!/usr/bin/env python
# coding: utf-8

# In[6]:

import numpy as np
import coin as c

class Payment_Management:
    """Klasa zarządzająca operacjami na pieniądzach"""
    
    def __init__(self):
        self.lista=np.array([])
        self.credit =0
        self.payment = 0
        
    def create_add_coin(self, value):
        def add_coin():
            coin = c.Coin(value)
            self.lista=np.append(self.lista,coin)
        return add_coin
    
    @property
    def get_sum(self):
        suma = 0
        for moneta in self.lista:
            suma+=moneta.get_value()
        return suma
    
    def return_coin(self, nominal):
        """Funckja usuwająca z listy zwracaną monetę"""
        if nominal in self.lista:
            self.lista = np.delete(self.lista, np.argwhere(self.lista == nominal)[0])
    
    def change(self, amount):
        """Funckja służąca do wydawania reszty"""
        self.lista=np.sort(self.lista)[::-1]
        temp_list = np.array([])
        i=0
        temp = 0
        while amount > temp and i < len(self.lista):
            if temp + self.lista[i].get_value() <= amount:
                temp_list=np.append(temp_list,self.lista[i])
                temp = temp + self.lista[i].get_value()
            i=i+1
        if temp != amount:
            
            return False
        for coin in temp_list:
            self.return_coin(coin)
        return temp_list
        
if __name__ == '__main__':
    pass
else:
    print('Management Payment imported succesfully')





