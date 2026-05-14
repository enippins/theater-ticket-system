import tkinter as tk
from tkinter import messagebox

class AccountGUI:
    def __init__(acct):
        #create account window
        acct.account_window = tk.Tk()
        acct.account_window.title("Account Creation")
        
        acct.account_window.minsize(width=300,height=300)
        acct.account_window.resizable(False,False)
        
        x_Left = int((acct.account_window.winfo_screenwidth() - 300)/2)
        y_Top = int((acct.account_window.winfo_screenheight() - 300)/2)
        acct.account_window.geometry("%dx%d+%d+%d" %(300,300,x_Left,y_Top))
        
        #create account label
        acct.account_window.account_label = tk.Label(acct.account_window,\
                                                      text="Create Account",\
                                                     font=("Century Schoolbook",15))                                            
        acct.account_window.account_label.place(x=80,y=10)
        
        #username entry controls
        acct.account_window.userName_entry = tk.Entry(acct.account_window,\
                                                      width=15, justify='left',\
                                                      font = ("Century Schoolbook",10))
        acct.account_window.userName_entry.place(x=120,y=60)
        acct.account_window.userName_entry.focus_force()

        #verifies it's a new username
        def verify_new_user(acct):
            valid = True
            newUser = (acct.account_window.userName_entry.get()) #get entry
            
            try:
                usernameFile = open("username.txt", 'r')
                for userTemp in usernameFile:
                    if newUser == userTemp.rstrip():
                        valid = False
                usernameFile.close()
                if(valid==False):
                    tk.messagebox.showinfo("Error","Username exists")
                    acct.account_window.userName_entry.focus_force()
                    acct.account_window.lift()
                else:
                    newUser = newUser + "\n"
                    verify_new_pass(newUser)
                    
            except IOError:
                print("no file exists")
                
        #username label
        acct.account_window.username_label = tk.Label(acct.account_window,\
                                                      text="username:",\
                                                      font=("Century Schoolbook",\
                                                            8))
        acct.account_window.username_label.place(x=60,y=60)



        #password entry controls
        acct.account_window.password_entry = tk.Entry(acct.account_window,\
                                                      width=15, justify='left',\
                                                      font = ("Century Schoolbook",10))
        acct.account_window.password_entry.place(x=120,y=170)

        #password label
        acct.account_window.password_label = tk.Label(acct.account_window,\
                                                      text="password:",\
                                                      font=("Century Schoolbook",\
                                                            8))
        acct.account_window.password_label.place(x=60,y=170)
        
        def verify_new_pass(newUser):
            newPass = (acct.account_window.password_entry.get())
            capLetter = False
            lowLetter = False
            num = False
            longEnough = False
            isValid = False
            try:
                if (len(newPass)>= 9):
                    longEnough = True
                for capL in newPass:
                    if capL.isupper():
                        capLetter = True
                        break
                for lowL in newPass:
                    if lowL.islower():
                        lowLetter = True
                        break
                for number in newPass:
                    if number.isdigit():
                        num = True
                        break
                if(longEnough == True and capLetter == True
                   and lowLetter == True and num == True):
                    isValid = True
                    tk.messagebox.showinfo("Success","Account Created!")
                    acct.account_window.destroy()
                    newPass = newPass + "\n"
                    saveInfo(newUser,newPass)
            
                else:
                    tk.messagebox.showinfo("Error","Invalid Password")
                    acct.account_window.userName_entry.focus_force()
                validity(isValid)
            except:
                print("This did not work")

               

            
        def saveInfo(newUser,newPass):
            usernameFile = open(r"username.txt", 'a')
            usernameFile.write(newUser)
            usernameFile.close()
            
            passwordFile = open(r"password.txt", 'a')
            passwordFile.write(newPass)
            passwordFile.close()
            
        def validity(isValid):
            boolFile = open(r"my_file.txt", 'w')
            if isValid == True:
                boolFile.write("True")
            else:
                boolFile.write("False")
            boolFile.close()

            

        #password requirement label
        acct.account_window.password_req = tk.Label(acct.account_window,\
                                                      text="Password must contain 9 characters,\
        \n1 digit, 1 uppercase letter, \nand 1 lowercase letter",\
                                                      font=("Century Schoolbook",\
                                                            8))
        acct.account_window.password_req.place(x=60,y=100)
        def cancelFn():
            isValid = False
            acct.account_window.destroy()
            validity(isValid)
        #cancel button
        acct.cancel_button=tk.Button(acct.account_window,\
                                     text="Cancel", width=8, font=("Century Schoolbook", 8),\
                                   command=cancelFn)
        acct.cancel_button.place(x=210,y=250)

        #create acct button
        def create_fn():
            verify_new_user(acct)
        acct.create_account_button=tk.Button(acct.account_window,\
                                   text="Create", width=8, font=("Century Schoolbook",\
                                                                8),command=create_fn)
        acct.create_account_button.place(x=30,y=250)





    
    
    
