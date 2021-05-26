#!/usr/bin/env python
# coding: utf-8

# In[1]:


def popup_window(tk, window, message):
    window = tk.Toplevel()
    label = tk.Label(window, text=message)
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')


# In[2]:


class InvalidArgument(Exception):
    """Ilość monet musi być dodatnia i całkowita"""
    def __init__(self, tk, window):
        self.mess = "Ilość monet musi być dodatnia i całkowita"
        popup_window(tk, window, self.mess)
        self.tm.clearList()
        super().__init__(self.mess)
        


# In[ ]:


class CannotChange(Exception):
    """Nie można wydać reszty"""
    def __init__(self, tk, window):
        self.mess = "Nie można wydać reszty. Tylko odliczona kwota"
        popup_window(tk, window, self.mess)
        super().__init__(self.mess)


# In[ ]:


class NotEnoughMoney(Exception):
    """Nie wystarczająca ilość pieniędzy"""
    def __init__(self, tk, window):
        self.mess = "Nie wystarczająca ilość pieniędzy"
        popup_window(tk, window, self.mess)
        super().__init__(self.mess)


# In[ ]:


class NoChangeNeeded(Exception):
    """Informacja o braku reszty do wypłacenia"""
    def __init__(self, tk, window):
        self.mess = "Brak reszty. Dziękujemy za zakupy"
        popup_window(tk, window, self.mess)

