import tkinter as tk

class newPass:
    def __init__(pw):
        #Create Window
        pw.passWin = tk.Toplevel()
        pw.passWin.title("Change Password")
        
        pw.passWin.minsize(width=300,height=300)
        pw.passWin.resizable(False,False)
        
        x_Left = int((pw.passWin.winfo_screenwidth() - 300)/2)
        y_Top = int((pw.passWin.winfo_screenheight() - 300)/2)
        pw.passWin.geometry("%dx%d+%d+%d" %(300,300,x_Left,y_Top))

        pw.passWin.account_label = tk.Label(pw.passWin,\
                                            text="Change Password",\
                                            font=("Century Schoolbook",15))                                            
        pw.passWin.account_label.place(x=60,y=10)
        
        #username entry controls
        pw.passWin.userName_entry = tk.Entry(pw.passWin,\
                                             width=15, justify='left',\
                                             font = ("Century Schoolbook",10))
        pw.passWin.userName_entry.place(x=120,y=70)
        pw.passWin.userName_entry.focus_force()
        #username label
        pw.passWin.username_label = tk.Label(pw.passWin,\
                                             text="username:",\
                                             font=("Century Schoolbook",8))
        pw.passWin.username_label.place(x=60,y=70)

        #password entry controls
        pw.passWin.old_pass = tk.Entry(pw.passWin,\
                                       width=15, justify='left',\
                                       font = ("Century Schoolbook",10))
        pw.passWin.old_pass.place(x=120,y=120)
        pw.passWin.new_pass = tk.Entry(pw.passWin,\
                                       width=15, justify='left',\
                                       font = ("Century Schoolbook",10))
        pw.passWin.new_pass.place(x=120,y=150)

        #password label
        pw.passWin.password_label1 = tk.Label(pw.passWin,\
                                                      text="Old password:",\
                                                      font=("Century Schoolbook",\
                                                            8))
        pw.passWin.password_label1.place(x=40,y=120)
        pw.passWin.password_label2 = tk.Label(pw.passWin,\
                                                      text="New password:",\
                                                      font=("Century Schoolbook",\
                                                            8))
        pw.passWin.password_label2.place(x=35,y=150)


        #password requirement label
        pw.passWin.password_req = tk.Label(pw.passWin,\
                                                      text="Password must contain 9 characters,\
        \n1 digit, 1 uppercase letter, \nand 1 lowercase letter",\
                                                      font=("Century Schoolbook",\
                                                            8))
        pw.passWin.password_req.place(x=60,y=200)


        def cancel_fn():
            pw.passWin.destroy()

        #cancel button
        pw.passWin.cancel_button=tk.Button(pw.passWin,\
                                     text="Cancel", width=8, font=("Century Schoolbook", 8),\
                                   command=cancel_fn)
        pw.passWin.cancel_button.place(x=210,y=260)
        
        #Verify new password
        def verify_new_pass(count):
            newPass = (pw.passWin.new_pass.get())
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
                    tk.messagebox.showinfo("Success","Password Changed!")
                    pw.passWin.destroy()

                    #Overwrite old password
                    newPass = newPass + "\n"
                    thisFile = open(r"password.txt", 'r')
                    thisList=thisFile.readlines()
                    thisList[count]=newPass.rstrip()+"\n"
                    
                    thisFile.close()
                    thisFile=open("password.txt",'w')
                    thisFile.writelines(thisList)
                    thisFile.close()

                    
                    cancel_fn
            
                else:
                    tk.messagebox.showinfo("Error","Invalid Password")
                    pw.passWin.new_pass.focus_force()
                    pw.passWin.lift()
    
            except:
                print("This did not work")
                
        #Verifying valid user/password combination
        def couldChange():
            validUser = False
            validLogin = False
            user = (pw.passWin.userName_entry.get()) #get user entry
            password =(pw.passWin.old_pass.get()) #get password entry
            count = 0
            
            try:
                usernameFile = open("username.txt", 'r')
                passwordFile = open(r"password.txt", 'r')
                usernameList =usernameFile.readlines()
                passwordList = passwordFile.readlines()
                for userTemp in usernameList: 
                    if user == userTemp.rstrip():
                        validUser=True
                        if password == passwordList[count].rstrip():
                            verify_new_pass(count)

                        else:
                            tk.messagebox.showinfo("Error","Wrong Password")
                            pw.passWin.lift()
                    else:
                        count+=1
                
                    
                usernameFile.close()
                
                
                passwordFile.close()
                if(validUser==False):
                    tk.messagebox.showinfo("Error","Username Does Not Exist")
                    pw.passWin.lift()

                    
            except IOError:
                print("no file exists")
                
        #Change password button        
        pw.passWin.change=tk.Button(pw.passWin,\
                                   text="Change", width=8, font=("Century Schoolbook",\
                                                                8),command=couldChange)
        pw.passWin.change.place(x=30,y=260)
