#!/usr/bin/env python
# coding: utf-8

# In[2]:


class RMS():

    def __init__(self,restaurant_name,restaurant_menu):
        self.total_bill=0
        self.paid_bill=0
        self.menu=restaurant_menu
        self.rest_name=restaurant_name
        self.user_order=""
        self.ask=""
        self.user_bill=0
        self.paid_bill=0
        self.user_pay=0
    
    # WELCOME USER
    def welcome_user(self):
        print("Welcome to ",self.rest_name)
    
    # DISPLAY MENU
    def display_menu(self):
        print("Menu : ")
        for i in self.menu:
            print(i.title(),self.menu[i])
    
    # TAKE ORDER
    def take_order(self):
        self.user_order=input("Please place your order here : ")
        
    # ASK FOR MORE ORDER
    def ask_more(self):
        self.ask=input("Do you want to order more : Y - Yes or N - No > ")
    
    # MORE ORDER FROM CUSTOMER
    def repeat_order(self):
        while(self.ask.lower()=="y"):
            if self.ask.lower()=="y":
                self.display_menu()
                self.take_order()
                if self.user_order.lower() in self.menu:
                    self.preparing_order()
                    self.serve_order()
                    self.ask_more()
                else:
                    print("INVALID ORDER")
            else:
                break
    
    # PREPARING ORDER
    def preparing_order(self):  
        print("Preparing your ",self.user_order.title())
        self.total_bill+=self.menu[self.user_order.lower()]
        import time
        time.sleep(3)
    
    # SERVE ORDER
    def serve_order(self):
        print("Your order is ready")
        print("Please enjoy your ",self.user_order.title())
    
    # DISPLAY BILL
    def display_bill(self):
        #user_bill=menu[user_order.lower()]
        print("Total Bill : ",self.total_bill)
        
    # TAKE BILL
    def take_payment(self):    
        self.user_pay=int(input("Please pay your bill here: "))
    
    # VERIFY PAYMENT
    def verify_payment(self):
        self.user_bill=self.total_bill
        if self.user_pay>self.user_bill:
            print("Payment Successful !!")
            print("Here is your change ",self.user_pay-self.user_bill)
        elif self.user_bill>self.user_pay:
            self.paid_bill=self.user_bill-self.user_pay
            print("Payment Unsuccessful  ")
            print("Please pay remaining amt ",self.paid_bill)
            while(self.paid_bill!=self.user_bill):
                self.take_payment()
                self.user_bill-=self.paid_bill
                if self.user_pay>self.paid_bill:
                    print("Payment Successful !!")
                    print("Here is your change ",self.user_pay-self.paid_bill)
                    break
                elif self.paid_bill>self.user_pay:
                    self.user_bill=self.paid_bill
                    self.paid_bill=self.user_bill-self.user_pay
                    print("Payment Unsuccessful  ")
                    print("Please pay remaining amt ",self.paid_bill)
                    if self.user_bill==0:
                        print("Payment successful !!")
                elif self.paid_bill==self.user_pay:
                    print("Payment succesful")
                    break
        else:
            print("Payment successful !!")
    
    # THANK USER
    def thank_user(self):
        print(f"Thank you for visiting {self.rest_name}! ")


    def order_process(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            self.ask_more()
            self.repeat_order()
            self.display_bill()
            self.take_payment()
            self.verify_payment()
            self.thank_user()
        else:
            print(self.user_order.title()," not in menu ")
            self.order_process()

if __name__=='__main__':
    rn='Ribbons & Balloons'
    rm={'black forest':400,'rasmalai':500,'white chocolate':350,'fresh fruits':550}

    rnb=RMS(rn,rm)

    import tkinter as tk
    window=tk.Tk()
    window.title('RMS')
    window.geometry('300x300')
    #tk.Label(window,text=rnb.rest_name,font=('Helvetica',16)).place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    tk.Label(window,text=rn,font=('Helvetica',16)).place(relx=0.5,rely=0.2,anchor=tk.CENTER)
    tk.Button(window,text="START ORDER",width=18,command=rnb.order_process).place(x=80,y=100)
    window.mainloop()


# In[ ]:


# In[ ]:




