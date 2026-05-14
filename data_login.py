import tkinter as tk


class LoginGui:
    def __init__(log):

        #login window
        
        log.login_window = tk.Toplevel()
        log.login_window.title("Login")
        
        log.login_window.minsize(width=300,height=300)
        log.login_window.resizable(False,False)
        
        x_Left = int((log.login_window.winfo_screenwidth() - 300)/2)
        y_Top = int((log.login_window.winfo_screenheight() - 300)/2)
        log.login_window.geometry("%dx%d+%d+%d" %(300,300,x_Left,y_Top))
        
        #login label
        log.login_window.account_label = tk.Label(log.login_window,\
                                                      text="Login",\
                                                     font=("Century Schoolbook",15))                                            
        log.login_window.account_label.place(x=130,y=10)
        
        #username entry controls
        log.login_window.userName_entry = tk.Entry(log.login_window,\
                                                      width=15, justify='left',\
                                                      font = ("Century Schoolbook",10))
        log.login_window.userName_entry.place(x=120,y=120)
        log.login_window.userName_entry.focus_force()
        #username label
        log.login_window.username_label = tk.Label(log.login_window,\
                                                      text="username:",\
                                                      font=("Century Schoolbook",\
                                                            8))
        log.login_window.username_label.place(x=60,y=120)

        #password entry controls
        log.login_window.password_entry = tk.Entry(log.login_window,\
                                                      width=15, justify='left',\
                                                      font = ("Century Schoolbook",10))
        log.login_window.password_entry.place(x=120,y=170)

        #password label
        log.login_window.password_label = tk.Label(log.login_window,\
                                                      text="password:",\
                                                      font=("Century Schoolbook",\
                                                            8))
        log.login_window.password_label.place(x=60,y=170)

        def cancel_fn():
            log.login_window.destroy()
            validLogin = False
            validateLogin(validLogin)

            
            
        #cancel button
        log.cancel_button=tk.Button(log.login_window,\
                                     text="Cancel", width=8, font=("Century Schoolbook", 8),\
                                   command=cancel_fn)
        log.cancel_button.place(x=210,y=250)
        
        def login_fn():
            validUser = False
            validLogin = False
            user = (log.login_window.userName_entry.get()) #get user entry
            password =(log.login_window.password_entry.get()) #get password entry
            count = 0
            
            try:
                usernameFile = open("username.txt", 'r')
                passwordFile = open(r"password.txt", 'r')
                usernameList =usernameFile.readlines()
                passwordList = passwordFile.readlines()
                for userTemp in usernameList: 
                    if user == userTemp.rstrip():
                        validUser = True
                        if password == passwordList[count].rstrip():
                                tk.messagebox.showinfo("Success","Login Successful!")
                                log.login_window.destroy()
                                validLogin = True
                                validateLogin(validLogin)
                                break
                        else:
                            tk.messagebox.showinfo("Error","Invalid Password")
                            log.login_window.lift()
                    else:
                        count+=1
                
                    
                usernameFile.close()
                
                
                passwordFile.close()
                if(validUser==False):
                    tk.messagebox.showinfo("Error","Username Does Not Exist")

                    log.login_window.userName_entry.focus_force()
                    log.login_window.lift()
                    
            except IOError:
                print("no file exists")
            
        def validateLogin(validLogin):
            boolFile = open(r"my_file.txt", 'w')
            if validLogin == True:
                boolFile.write("True")
            else:
                boolFile.write("False")
            boolFile.close()
                
                
        #login button
        log.login_button=tk.Button(log.login_window,\
                                   text="Login", width=8, font=("Century Schoolbook",\
                                                                8),command=login_fn)
        log.login_button.place(x=30,y=250)

        
        #image
        photo = tk.PhotoImage(file="theater logo smaller.png")
        log.labelGif=tk.Label(log.login_window, image=photo)
        log.labelGif.image = photo
        log.labelGif.place(x=110,y=40)

        
        
        


