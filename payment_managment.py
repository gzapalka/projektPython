#!/usr/bin/env python
# coding: utf-8

# In[1]:


from  coin import *
import numpy as np
from decimal import *

class Payment_Management:
    """Klasa obsługująca logikę zarządzania pieniędzmi"""
    
    def __init__(self) -> None:
        """Zwraca obiekt typu Payment_Management"""
        self.numberText: tk.StringVar
        expectedValue = [50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
        self.expectedValue= [Decimal(expectedValue[i]).quantize(Decimal('0.00')) for i in range(len(expectedValue))]
        self.lista=np.array([])
        self.credit =0
        self.payment = 0
        
    def add_coin(self, value: float) -> None:
        """Dodaje monetę do schowka"""
        self.lista=np.append(self.lista,Coin(value))
        self.payment+=Decimal(value)
            
    def get_sum(self) -> Decimal:
        """Zwraca łączną wartość znajdujących się w automacie monet"""
        return np.sum([coin.get_value for coin in self.lista])
    
    def return_coin(self, coin: Coin) -> None or bool:
        """Usuwa monetę z listy jeżeli się na niej znajduje"""
        if coin in self.lista:
            self.lista = np.delete(self.lista, np.argwhere(self.lista == coin)[0])
        else:
            return False
            
    def change(self, amount: Decimal) -> np.array or bool:
        """Wydaje resztę jeżeli to możliwe"""
        self.lista=np.sort(self.lista)[::-1]
        temp = 0
        temp_list = np.array([])
        i=0
        while amount > temp and i < len(self.lista):
            if temp + self.lista[i].get_value <= amount:
                temp_list = np.append(temp_list, self.lista[i])
                temp = temp+ self.lista[i].get_value
            i=i+1
            
        if temp != amount:
            return False
        
        for coin in temp_list:
            self.return_coin(coin)
        return temp_list
    
    @property
    def get_payment(self) -> Decimal:
        """Zwraca łączną wartość wrzuconych monet"""
        return self.payment
    
    @property
    def get_credit(self) -> Decimal:
        """Zwraca wartość należnej zapłaty"""
        return self.credit
    
    @property
    def get_amount_to_pay(self) -> Decimal:
        """Zwraca wartość należnej reszty"""
        return self.payment - self.credit
        
if __name__ == '__main__':
    pass
else:
    print('Management Payment imported succesfully')


# In[ ]:




