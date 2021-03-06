#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk


# In[1]:


def popup_window(window, message) -> None:
    """Tworzy okno typu pop-up dla customowych wyjątków"""
    window = tk.Toplevel()
    label = tk.Label(window, text=message)
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')


# In[2]:


class InvalidArgument(Exception):
    """Ilość monet musi być dodatnia i całkowita"""
    def __init__(self,gui = None):
        self.mess = "Ilość monet musi być dodatnia i całkowita"
        if not(gui is None):
            popup_window(gui.window, self.mess)
        super().__init__(self.mess)
        


# In[ ]:


class CannotChange(Exception):
    """Nie można wydać reszty"""
    def __init__(self,window, added):
        self.mess = "Nie można wydać reszty. Tylko odliczona kwota \n\n Zwracam: " + (str)(added[1])
        popup_window(window, self.mess)
        super().__init__(self.mess)


# In[ ]:


class NotEnoughMoney(Exception):
    """Nie wystarczająca ilość pieniędzy"""
    def __init__(self,window):
        self.mess = "Nie wystarczająca ilość pieniędzy"
        popup_window(window, self.mess)
        super().__init__(self.mess)