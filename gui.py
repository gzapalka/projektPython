#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import numpy as np

class GUI:
    
    def __init__(self, tm):
        tm.gui  = self
        self.display_paymnet_layout = False
        self.tm = tm
        self.window = tk.Tk()
        self.window.geometry("450x450")

        header_frame = tk.Frame(self.window, width = 100, height = 50)
        header_frame.grid(row=0, column=0, padx=10, pady=5)
        tk.Label(header_frame, text="Choose Ticket").grid(row=0, column=0, padx=170, pady=5)
        
        end = tk.Button(text = "Zrezygnuj", width=7,height=1,bg="grey",fg="white", bd=5,
                        command = lambda:[self.tm.resign(), self.update_credit_status(), self.update_payment_status()])
        end.place(x = 350, y = 10)
        self.printTicketLayout()  
        self.window.mainloop()
        
   
    def update_credit_status(self) -> None:
        """Wyświetla obecne zadłużenie"""
        if self.display_paymnet_layout == False:
            self.printPaymentLayout()
            self.clearEntry()
            self.display_paymnet_layout = True
        credit_info = "Do zapłaty: " + (str)(self.tm.get_credit) + " zł"
        self.credit.set(credit_info)
        
    def printTicketLayout(self):
        normalTicketLabel = tk.Label(text="Normalne", foreground="white", background="grey",width=30, height=3)
        normalTicketLabel.place(x=5, y =60)
        ticket_value = [3,4,5,2,3,4]
        button_tickets = ["20min\n3zł","40min\n4zł","60min\n5zł","20min\n2zł","40min\n3zł","60min\n4zł"]
        
        button_func = [self.tm.create_add_ticket(ticket_value[i]) for i in range(6)]
        buttons = np.array([tk.Button(text = button_tickets[i], width=5,height=3,bg="grey",fg="white", bd=5,
                                      command = lambda button_f = button_func[i]: [button_f(), self.update_credit_status()])
                   for i in range(len(button_tickets))])
        
        for i in range(len(buttons)):
            if i < len(buttons)//2:
                buttons[i].place(x = 40 + i * 50, y=120)
            elif i == len(buttons)//2:
                reducedTicketLabel = tk.Label(text="Ulgowe", foreground="white", background="grey",width=30, height=3)
                reducedTicketLabel.place(x=230, y=60)
                buttons[i].place(x = 110 +i*50, y=120)
            else:
                buttons[i].place(x = 110 + i*50, y=120)
       
        self.credit = tk.StringVar()
        credit_info = "Do zapłaty: 0 zł"
        self.credit.set(credit_info)
        credit_status = tk.Label(textvariable = self.credit, foreground="white", background="grey",width=12, height=1)
        credit_status.place(x=5, y=190)
        
    def setPlace(self, n):
        for i in range(n):
            yield 40 + n * 100
        
    def readDataFromEntries(self):
        entryData = [self.e[i].get() for i in range(len(self.e))]
        return entryData
    
    def placeButtons(self) -> None:
        """Wyświetla ekran płatniczy"""
        
        button_coin = ['50 zł','20 zł','10 zł','5 zł','2 zł','1 zł','50 gr','20 gr','10 gr','5 gr','2 gr','1 gr']
        buttons = [tk.Button(text = button_coin[i], width=3,height=1,bg="grey",fg="white", bd=5) for i in range(len(button_coin))]
        place_x = [40,140,240]
        place_y = [220, 260, 300, 340]
        buttons[0].place(x=40, y=220)
        buttons[1].place(x=140, y=220)
        buttons[2].place(x=240, y=220)
        buttons[3].place(x=40, y=260)
        buttons[4].place(x=140, y=260)
        buttons[5].place(x=240, y=260)
        buttons[6].place(x=40, y=300)
        buttons[7].place(x=140, y=300)
        buttons[8].place(x=240, y=300)
        buttons[9].place(x=40, y=340)
        buttons[10].place(x=140, y=340)
        buttons[11].place(x=240, y=340)
        
        self.confirm_button=tk.Button(text = "Zatwierdź", width=10,height=1,bg="grey",fg="white", bd=5, command = self.tm.manageChange)
        self.confirm_button.place(x=5, y = 410)
    
    def clearEntry(self):
        for i in self.e:
            i.insert(1,"0")
            
    
    def placeEntryWidget(self):
        e = [tk.Entry(self.window,width=5) for i in range(12)]
        e[0].place(x=90, y=230)
        e[1].place(x=190, y=230)
        e[2].place(x=290, y=230)
        e[3].place(x=90, y=270)
        e[4].place(x=190, y=270)
        e[5].place(x=290, y=270)
        e[6].place(x=90, y=310)
        e[7].place(x=190, y=310)
        e[8].place(x=290, y=310)
        e[9].place(x=90, y=350)
        e[10].place(x=190, y=350)
        e[11].place(x=290, y=350)
        self.e = e
        
    def printPaymentLayout(self):
        self.placeButtons()
        self.placeEntryWidget()  
        
        
if __name__ == '__main__':
    pass
else:
    print('GUI imported succesfully')


# In[ ]:




