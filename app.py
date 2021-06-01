#!/usr/bin/env python
# coding: utf-8

# In[5]:


# from tkinter.constants import BOTH
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
from typing import Callable
import handler
import exceptions

class App(tk.Frame):
    
    def __init__(self) -> None:
        """Tworzy obiekt typu app"""
        self.handler = handler.Handler()
        window = tk.Tk()
        super().__init__(window)
        self.window = window
        self.window.title('Ticket Machine')
        self.window.geometry('500x300')
        self.display_screen()
        self.mainloop()
        
    def update_info(self)-> None:
        """Uaktualnie infomacje o należnej płatności"""
        credit_info = (str)(self.handler.get_credit)+ " zł"
        self.credit_info.set(f'{credit_info}')
        if self.entries_enabled == False:
            self.switch_entries_enabale(True)
            
    def clear_entries(self)-> None:
        for entry in self.entries:
                entry.delete(0, tk.END)
                entry.insert(1, "0")
        
    def switch_entries_enabale(self,display: bool)-> None:
        """Włącza możliwość wrzucania monet"""
        self.entries_enabled = display
        if display:
            for entry in self.entries:
                entry.configure(state="normal")
        else:
            for entry in self.entries:
                entry.delete(0, tk.END)
                entry.insert(1, "0")
                entry.configure(state="disabled")
            
    def display_screen(self) -> None:
        """Wyświetla elementy GUI"""
        for i in range(8):
            self.grid_columnconfigure(i, pad=2, weight=1)

        label = tk.Label(self, text="Wybierz bilet:",width = 8)
        label.grid(row=0, column = 0, columnspan=2, rowspan=1, sticky=tk.W+tk.E+tk.N+tk.S)
        label = tk.Label(self, text="Wrzuć monetę:")
        label.grid(row=0, column=3, columnspan=2, rowspan=1, sticky=tk.W+tk.E+tk.N+tk.S)
        
        self.create_keypad(0, 0, self.handler.create_add_ticket, self.handler.available_tickets, 3)
        self.create_keypad(4, 3, None, self.handler.expectedValue[:6], 1)
        self.create_keypad(4, 5, None, self.handler.expectedValue[6:], 1)
        
        self.create_entries()
        
        button = tk.Button(self, text='Wrzuć monety', command=self.insert_coins)
        button.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=2, pady=2)
        button = tk.Button(self, text='Zakończ płatność', command=self.confirm_payment)
        button.grid(row=5, column=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=2, pady=2)
        button = tk.Button(self, text='Zrezygnuj', command=self.resign)
        button.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=2, pady=2)
        
        self.credit_info = tk.StringVar()
        self.payment_info = tk.StringVar()
        
        label = tk.Label(self, text="Do zapłaty:")
        label.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=2, pady=2)
        credit_label = tk.Label(self, textvariable=self.credit_info)
        credit_label.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=2, pady=2)
        
        self.pack(fill="both", expand=True)
        
    def popup_window(self, message: str) -> None:
        """Wyświetla okno typu pop-up z informacją o przebiegu tranzakcji"""
        self.window = tk.Toplevel()
        label = tk.Label(self.window, text=message)
        label.pack(fill='x', padx=50, pady=5)

        button_close = tk.Button(self.window, text="OK", command=self.window.destroy)
        button_close.pack(fill='x')
        
    def insert_coins(self) -> None:
        entry_data = self.read_data_from_entries()
        try:
            self.handler.insert_coins(entry_data)
            self.clear_entries()
        except exceptions.InvalidArgument:
            self.resing()

    def confirm_payment(self) -> None:
        """Rozlicza płatność"""
        entry_data = self.read_data_from_entries()
        if self.handler.check_data(entry_data):
            try:
                change = self.handler.manage_change(entry_data, self)
                if type(change) == tuple:
                    raise exceptions.CannotChange(self, change)
                self.popup_window("Dziękujemy za zakupy!\n\n Twoja reszta: " +
                                  (str)(change) +"\nKupiono: " + (str)(self.handler.bought_ticket))
            except (exceptions.NotEnoughMoney, exceptions.CannotChange):
                pass
        else:
            self.resign()
            raise exceptions.InvalidArgument(self)
        self.resign(True)
        
        
    def resign(self, correct_transaction = False) -> None:
        """Usuwa dane tranzakcji"""
        self.handler.resign()
        self.update_info()
        self.switch_entries_enabale(False)
        if not correct_transaction:
            self.popup_window("Zwracam monety: " + (str)(self.handler.added_coins))
        self.handler.added_coins = []
    
    def read_data_from_entries(self) -> list:
        """Czyta ilość wrzuconych monet"""
        entryData = [self.entries[i].get() if self.entries[i].get()!="" else "0" for i in range(len(self.entries))]
        return entryData
    
    def create_entries(self) -> None:
        """Tworzy widgety do wpisywania ilość wrzucanych monet"""
        self.entries_enabled = False
        self.entries = [tk.Entry(self, justify='right',width = 3, state=tk.DISABLED) for i in range(len(self.handler.expectedValue))]
        self.place_entries(4,4,0,6,1)
        self.place_entries(4,6,6,12,1)
        
        
    def place_entries(self, n_row: int, n_column: int, first_index: int, last_index: int, column_number: int) -> None:
        """Rozmieszcza widgety typu entry"""
        start_row = n_row + 2
        i = 0
        for e in self.entries[first_index:last_index]:
            e.grid(row = start_row - (i // column_number), column=i % column_number + n_column, sticky=tk.W+tk.E+tk.N+tk.S, padx=2, pady=2)
            i+=1
            
    def create_keypad(self, n_row: int, n_column: int, func: Callable, values: list, column_number: int) -> None:
        """Wyświeltla listę dostępnych biletów i monet"""
        start_row = n_row + 2
        button_func = [self.handler.create_add_ticket(self.handler.ticket_values[i], self.handler.available_tickets[i]) for i in range(len(self.handler.ticket_values))]
        for i in range(len(values)):
            if(func != None):
                button = tk.Button(self, text=f'{values[i]}',width = 8, height = 2, command=lambda button_f = button_func[i]: [button_f(), self.update_info()])
            else:
                button = tk.Button(self, text=f'{values[i]}',height = 2, state = tk.DISABLED)
            button.grid(row=start_row - (i // column_number), column=i % column_number + n_column, sticky=tk.W+tk.E+tk.N+tk.S, padx=2, pady=2) 
        
if __name__ == '__main__':
    App()
else:
    print("App imported succesfully")

