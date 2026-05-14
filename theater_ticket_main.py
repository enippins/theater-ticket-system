import tkinter as tk
from tkinter import *
import time

import data_create_acct
import data_login
import sales
import change_pass

class DataGUI:
    def __init__(self):
        #Reset matinee bought seats
        thisFile=open("seatsBought1.txt",'r')
        thisList=thisFile.readlines()
        count = 0
        for line in thisList:
            thisList[count]="0\n"
            count+=1
        thisFile.close()
        thisFile=open("seatsBought1.txt",'w')
        thisFile.writelines(thisList)
        thisFile.close()
        
        #Reset evening bought seats
        thisFile=open("seatsBought2.txt",'r')
        thisList=thisFile.readlines()
        count = 0
        for line in thisList:
            thisList[count]="0\n"
            count+=1
        thisFile.close()
        thisFile=open("seatsBought2.txt",'w')
        thisFile.writelines(thisList)
        thisFile.close()
        
        #create main window
        self.main_win = tk.Tk()
        self.main_win.title("Mosaic Theatre Kiosk Program")
        self.main_win.minsize(width=600,height=400)
        self.main_win.resizable(False,False)
        
        x_Left = int((self.main_win.winfo_screenwidth() - 600)/2)
        y_Top = int((self.main_win.winfo_screenheight() - 400)/2)
        self.main_win.geometry("%dx%d+%d+%d" %(600,400,x_Left,y_Top))
        
        #heading label for window
        self.heading_label = tk.Label(text="Mosaic Theatre", \
                                      font=("Viner Hand ITC",30),fg="sandybrown")                  
        self.heading_label.place(x=175,y=20)

        #description label
        self.descr_label = tk.Label(text="Management System",\
                                    font=("Century Schoolbook",12))
        self.descr_label.place(x=225,y=70)

        #cancel button
        self.cancel_button=tk.Button(text="Cancel", width=16, font=("Century Schoolbook", 10),\
                                   command=self.main_win.destroy)
        self.cancel_button.place(x=400,y=310)

        #function to create login window
        def login():
            LoginWin = data_login.LoginGui()
            self.create_acct_button.config(state="disabled")
            self.login_button.config(state="disabled")
            self.cancel_button.config(state="disabled")
            LoginWin.login_window.wait_window()
            valid()


        #login button
        self.login_button = tk.Button(text="Login", width=16,font=("Century Schoolbook",10),\
                                      command=login)
        self.login_button.place(x=250,y=310)
    
        #function to create the account creatation window
        def create_account():
            CreateAcctWin = data_create_acct.AccountGUI() #create the win
            self.create_acct_button.config(state="disabled")
            self.login_button.config(state="disabled")
            self.cancel_button.config(state="disabled")
            CreateAcctWin.account_window.wait_window()
            valid()
            
        #Validates successful create account/login   
        def valid():
            boolFile = open(r"my_file.txt", 'r')
            if boolFile.readline() == "True":
                #Destroy old controls
                self.cancel_button.destroy()
                self.login_button.destroy()
                self.create_acct_button.destroy()
                self.labelPhoto.destroy()
                mainInt()
            else:
                unTrue()
            boolFile.close()
            
        #If unsuccessful, buttons return to normal
        def unTrue():
            self.create_acct_button.config(state="normal")
            self.login_button.config(state="normal")
            self.cancel_button.config(state="normal")
            
        #If successful, user interface created       
        def mainInt():


            #Select time
            logo = tk.PhotoImage(file="theater logo medium.png")
            self.smallLogo=tk.Label(image = logo)
            self.smallLogo.image = logo
            self.smallLogo.place(x=190,y=95)
            self.optionsText = tk.Label(text = "Select your time:",\
                                        font=("Century Schoolbook", 15))
            self.optionsText.place(x=225, y=250)
            self.select_button = tk.Button(text="Select", width=16,font=("Century Schoolbook",\
                                                                         10),bg=("sandybrown"),command=selectButton)
            self.select_button.place(x=235,y=340)
            self.radio_var = tk.StringVar()
            self.radio_var.set('Matinee')
            self.mat_pricing = tk.Radiobutton(text="Matinee pricing",font=("Century Schoolbook",12),\
                                              variable = self.radio_var, value='Matinee')
            self.mat_pricing.place(x=135,y=290)
            self.evening_pricing = tk.Radiobutton(text="Evening pricing",font=("Century Schoolbook",12),\
                                              variable = self.radio_var, value='Evening')
            self.evening_pricing.place(x=320,y=290)

            #Manager functions function
            def mgrFn(*args):
                mgrCode = "010623" #Code
                #Code entry window
                self.code_entry = tk.Tk()
                self.code_entry.title("Manager")
                self.code_entry.minsize(width=230,height=100)
                self.code_entry.resizable(False,False)
                x_Left = int((self.code_entry.winfo_screenwidth() - 200)/2)
                y_Top = int((self.code_entry.winfo_screenheight() - 100)/2)
                self.code_entry.geometry("%dx%d+%d+%d" %(200,100,x_Left,y_Top))
                
                #Code entry
                self.code_entry.enterCode = tk.Entry(self.code_entry, width=15,\
                                                     justify='left', font=("Century Schoolbook",10))
                self.code_entry.enterCode.place(x=50,y=40)
                self.code_entry.enterCode.focus_force()
                self.code_entry.codeLabel=tk.Label(self.code_entry,\
                                                   text="Enter code:",font=("Century Schoolbook",\
                                                                            10), width=10)
                self.code_entry.codeLabel.place(x=50,y=15)
                
                #Enter button function
                def enter():
                    tempCode=self.code_entry.enterCode.get()
                    self.code_entry.destroy()
                    if tempCode==mgrCode:
                        selections=self.option_var.get()
                        if selections == "Sales":
                            SalesWin = sales.SalesGUI()
                        if selections == "Change Password":
                            PassWin = change_pass.newPass()
                #Enter button for code entry
                self.code_entry.enterBtn=tk.Button(self.code_entry, text="Enter",font=\
                                                   ("Century Schoolbook",10),\
                                                   command=enter)
                self.code_entry.enterBtn.place(x=100,y=70)
                
            #Manager options   
            optionList = ("Sales","Change Password")
            self.option_var = tk.StringVar()
            self.option_var.set("Manager Functions")
            self.option_menu = tk.OptionMenu(self.main_win, self.option_var, *optionList, command=mgrFn)
            self.option_menu.place(x=5, y=5)
            
                    
        #Once button selected    
        def selectButton(): 
            if str(self.radio_var.get()) == "Matinee": #Matinee prices
                #if past time of showing, unavailable to user
                if int(time.strftime("%H")) >= 18:
                    tk.messagebox.showinfo("Error","Unavailable\n\nShow started at 2pm")
                else:
                    nextTime = "14:00"
                    Available(nextTime)
            else: #Evening prices
                
                #if past time of showing, unavailable to user
                if int(time.strftime("%H")) >= 23:
                    tk.messagebox.showinfo("Error","Unavailable\n\nShow started at 8pm")
                else:
                    nextTime = "20:00"
                    Available(nextTime)
        #If the showtime is available
        def Available(nextTime):
            #destroy old controls
            self.select_button.destroy()
            self.mat_pricing.destroy()
            self.evening_pricing.destroy()
            self.optionsText.destroy()
            self.smallLogo.destroy()
            self.descr_label.destroy()
            self.heading_label.destroy()
    
            #Seating
            theater_image = tk.PhotoImage(file="Theater.png")
            self.GIF = tk.Label(image=theater_image)
            self.GIF.image= theater_image
            self.GIF.place(x=5,y = 5)
            
            #Displays time of next showing
            self.next_showing = tk.Label(text="Next showing at: " + nextTime, font=("Century Schoolbook",\
                                                                  10))
            self.next_showing.place(x=400,y=50)
            file = 0
            #Which file to open for seating
            if nextTime == "14:00" :
                priceFile = open("MatPricing.txt", 'r')
                seatsFile=open("seatsBought1.txt",'r')
                file = 1
            else:
                priceFile = open("EveningPricing.txt", 'r')
                seatsFile=open("seatsBought2.txt",'r')
                file = 2
            tempList = priceFile.readlines()
            priceFile.close()
            
            #Remove \n
            count = 0
            for line in tempList:
                tempList[count]= line.rstrip()
                count += 1
            #Remove ;    
            count = 0
            for line in tempList:
                tempList[count]= line.split(";")
                count += 1
            
            #Create Lists
            seatList = [0]
            priceList = [0]
            amountList = [0]
            
            #File for number of seats bought
            
            seatsBought = seatsFile.readlines()
            seatsFile.close()

            #Remove \n for seatsbought
            count = 0
            for line in seatsBought:
                seatsBought[count]=line.rstrip()
                count+=1
            #Fill the main lists
            count=0
            for line in tempList:
                filler = tempList[count][0]
                prices = tempList[count][1]
                amounts = tempList[count][2]
                count += 1
                seatList.append(filler)
                priceList.append(prices)
                amountList.append(amounts)
            #Remove 0
            seatList.remove(0)
            priceList.remove(0)
            amountList.remove(0)
            #List for bought seats
            boughtSeats=[0]
            count=0
            for line in seatsBought:
               bought=seatsBought[count]
               count+=1
               boughtSeats.append(bought)
            boughtSeats.remove(0)

            
            #Number of seats - bought seats
            count=0
            for line in boughtSeats:
                bought=line
                totalSeats=int(amountList[count])-int(bought)
                amountList[count]=str(totalSeats)
                count+=1
            
            #Frame for button cluster 
            seat = list(range(len(seatList)))
            index=0
            self.lf = tk.LabelFrame(text = "Choose a button.", padx=6, pady=16,\
                                    bd=4, relief= SUNKEN)
            self.lf.grid(row= 1, rowspan=4, column = 1, columnspan=4)
            self.lf.place(x=340,y=80)
            keyRow=0
            keyCol=0
            seatNum= ""
            for seatNum in seatList:
                #Button cluster for available seats
                cmd = lambda seat_num = seatNum, seatprice = priceList[index],\
                      amount=amountList[index],val=index:button_clicked(seat_num,seatprice,amount,val)
                
                #Create label/button
                self.priceLabel = tk.Label(text="",font=("Century Schoolbook",10),\
                                           width=10)
                self.purchaseButton = tk.Button()

                #Function for button cluster
                def button_clicked(seat_num,seatprice,amount,val):
                    for button in seat:
                        button.config(bg="lightgray")
                    if amount == "0":
                        tk.messagebox.showinfo("Error","No more seats are\navailable for this section:\n\n"+seat_num)
                    else:
                        seat[val].config(bg="sandybrown")
                    #Modify/place price
                        self.priceLabel.config(text=seatprice,font=("Century Schoolbook",11),\
                                          width=10)
                        self.priceLabel.place(x=420,y=275)
                    
                    #Purchase button function
                    def purchase():
                        #Ticket stub window
                        self.ticketStub= tk.Tk()
                        self.ticketStub.title=("Ticket Stub")
                        self.ticketStub.minsize(width=300,height=300)
                        self.ticketStub.resizable(False,False)
                        x_Left = int((self.ticketStub.winfo_screenwidth() - 300)/2)
                        y_Top = int((self.ticketStub.winfo_screenheight() - 300)/2)
                        self.ticketStub.geometry("%dx%d+%d+%d" %(300,300,x_Left,y_Top))
                        
                        #Okay button function
                        def ticketOK():
                            self.ticketStub.destroy()
                            goBack()
                        #Ticket stub labels
                        self.ticketStub.tixStub1=tk.Label(self.ticketStub,\
                                                          text="Mosaic Theater",font=("Century Schoolbook",17),fg="sandybrown",\
                                                          width=20)
                        self.ticketStub.tixStub1.place(x=10,y=20)
                        
                        self.ticketStub.tixStub2=tk.Label(self.ticketStub,\
                                                          text="Ticket Stub",font=("Century Schoolbook",12),\
                                                          width=20)
                        self.ticketStub.tixStub2.place(x=60,y=50)
                        
                        self.ticketStub.seating=tk.Label(self.ticketStub,\
                                                          text="Seating for sections "+seat_num,font=("Century Schoolbook",10),\
                                                          width=30)
                        self.ticketStub.seating.place(x=30,y=100)
                        
                        self.ticketStub.price=tk.Label(self.ticketStub,\
                                                          text="Price: "+seatprice,font=("Century Schoolbook",10),\
                                                          width=30)
                        self.ticketStub.price.place(x=30,y=130)
                        
                        self.ticketStub.time=tk.Label(self.ticketStub,\
                                                          text="Time: "+nextTime,font=("Century Schoolbook",10),\
                                                          width=30)
                        self.ticketStub.time.place(x=30,y=150)
                        
                        self.ticketStub.description=tk.Label(self.ticketStub,\
                                                          text="Seating is general admission "+\
                                                             "for all sections.\nThis ticket is "+\
                                                             "non-transferable.\nAll rights reserved.",\
                                                             font=("Century Schoolbook",10),\
                                                          width=35)
                        self.ticketStub.description.place(x=10,y=170)
                        
                        #Okay button
                        self.ticketStub.okButton=tk.Button(self.ticketStub,text="Ok",font=("Century Schoolbook",10),width=10,\
                                                           command=ticketOK)
                        self.ticketStub.okButton.place(x=110,y=250)
                        

                        #Increase number of bought seats
                        if file == 1:
                            thisFile=open("seatsBought1.txt",'r')
                            thisList=thisFile.readlines()
                            num=int(thisList[val])
                            num+=1
                            thisList[val]=str(num)+"\n"
                            thisFile.close()
                            thisFile=open("seatsBought1.txt",'w')
                            thisFile.writelines(thisList)
                            thisFile.close()
                            
                        if file == 2:
                            thisFile=open("seatsBought2.txt",'r')
                            thisList=thisFile.readlines()
                            num=int(thisList[val])
                            num+=1
                            thisList[val]=str(num)+"\n"
                            thisFile.close()
                            thisFile=open("seatsBought2.txt",'w')
                            thisFile.writelines(thisList)
                            thisFile.close()
                        
                        
                    #Purchase button modification/placement
                    if amount != "0":
                        self.purchaseButton.config(text="Purchase", font=("Century Schoolbook",\
                                                           10),width=10,bg="sandybrown",command=purchase)
                        self.purchaseButton.place(x=420,y=310)
                    
                seat[index] = tk.Button(self.lf,text=seatNum, font =("Century Schoolbook",10),\
                                             height=2,width=13,bd=3,bg="lightgray",command=cmd)
                seat[index].grid(row=keyRow,column=keyCol)
                index = index+1
                keyCol = keyCol +1
                if keyCol > 1:
                    keyCol = 0
                    keyRow= keyRow+1
            #Back button for purchase screen
            def goBack():
                index= 0
                for seatNum in seatList:
                    seat[index].destroy()
                    index+=1
                self.backBtn.destroy()
                self.lf.destroy()
                self.next_showing.destroy()
                self.GIF.destroy()
                self.priceLabel.destroy()
                self.purchaseButton.destroy()
                mainInt()
            
                
                #heading label for window
                self.heading_label = tk.Label(text="Mosaic Theatre", \
                                      font=("Viner Hand ITC",30),fg="sandybrown")                  
                self.heading_label.place(x=175,y=20)

                #description label
                self.descr_label = tk.Label(text="Management System",\
                                    font=("Century Schoolbook",12))
                self.descr_label.place(x=225,y=70)
            self.backBtn = tk.Button(text="Back", font=("Century Schoolbook",10),\
                                     width=5, command=goBack)
            self.backBtn.place(x=550,y=350)

                    
        
        #create account button
        self.create_acct_button=tk.Button(text="Create Account", width=16,font=("Century Schoolbook",10),\
                                         command=create_account)
        self.create_acct_button.place(x=100,y=310)

        #image
        photo = tk.PhotoImage(file="theater logo.png")
        self.labelPhoto=tk.Label(image= photo)
        self.labelPhoto.image = photo
        
        self.labelPhoto.place(x=160,y=100)

        #Current time
        def timing():
            current_time = time.strftime("%H : %M")
            self.clock.config(text=current_time)
            self.clock.after(100,timing)
            
        self.clock=tk.Label(font=("Cenutry Schoolbook",15), width = 10)
        self.clock.place(x=500,y=10)
        timing()
        
        


        tk.mainloop()
mainWin = DataGUI()

