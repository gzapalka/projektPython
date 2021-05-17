#!/usr/bin/env python
# coding: utf-8

# In[6]:


import coin as c

class Payment_Menagement:
    
    def __init__(self):
        self.obsluguje=[0.01,0.02, 0.05, 0.1,0.2,0.5,1,2,5,10,20,50]
        self.lista=np.array([])
        self.credit =0
        self.payment = 0
        
    def add_coin(self, coin):
        if isinstance(coin, c.Coin):
            self.lista=np.append(self.lista,coin)
        else:
            print('to nie moneta')
            
    def get_sum(self):
        suma = 0
        for moneta in self.lista:
            suma+=moneta.get_value()
        return suma
    
    def return_coin(self, nominal):
        if nominal in self.lista:
            self.lista = np.delete(self.lista, np.argwhere(self.lista == nominal)[0])
    
    def change(self, amount):
        self.lista=np.sort(self.lista)[::-1]
        temp = 0
        temp_list = []
        i=0
        while amount > temp and i < len(self.lista):
            if temp + self.lista[i].get_value() <= amount:
                temp_list.append(self.lista[i])
                temp = temp+ self.lista[i].get_value()
            i=i+1
        if temp != amount:
            sg.popup("Tylko odliczona kwota!")
            return False
        for coin in temp_list:
            self.return_coin(coin)
        return temp_list
        
if __name__ == '__main__':
    pass
else:
    #Nie - plik został zaimportowany jako moduł
    print('Management Payment imported succesfully')


# In[ ]:




