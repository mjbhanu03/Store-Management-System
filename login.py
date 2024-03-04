from tkinter import * 
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import os
import email_pass
import smtplib
import time

class loginSystem:
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Stock Management System | Developed by JI")
        
        # ==== Variables ====
        self.var_name = StringVar()
        self.var_pass = StringVar()
        self.otp = ''

        # ==== images ====
        # self.phone_image = PhotoImage(file="images/iphone15.png")
        # self.lbl_phone_image = Label(self.root,image=self.phone_image).place(x=200,y=110)
        
        # ==== Login Page ====
        login_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        login_frame.place(x=500,y=150,width=350,height=460)
    
        title = Label(login_frame,text="Login",font=('Elephant',20,'bold'),bg='white').place(x=0,y=30,relwidth=1)
        
        lbl_user = Label(login_frame,text="Username",font=("Andalus",12),bg="white",fg="#767171").place(x=50,y=115)
        txt_username = Entry(login_frame,textvariable=self.var_name,font=("times new roman",15),bg="#d4d4d4").place(x=50,y=155,width=250) 

        lbl_pass = Label(login_frame,text="Password",font=("Andalus",12),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass = Entry(login_frame,textvariable=self.var_pass,show="*",font=("times new roman",15),bg="#d4d4d4").place(x=50,y=240,width=250) 
        
        btn_login = Button(login_frame,text="Log In",font=('Aarial Rounded MT Bold',15,'bold'),bg="#3c4491",fg="white",activebackground="#3c4491",activeforeground="white",cursor="hand2",command=self.login).place(x=50,y=300,width=250,height=35)
        
        hr = Label(login_frame,bg='lightgrey').place(x=50,y=360,width=250,height=2)
        jistore = Button(login_frame,text="Forgot Password?",font=('times new roman',15,'bold'),cursor="hand2",bd=0 ,bg='white',fg='blue',command=self.forget).place(x=100,y=380)
        
    def login(self):
        con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
        cursor = con.cursor()
        
        try:
            if self.var_name.get() == '' or self.var_pass.get() == '':
                MessageBox.showerror('Error','All field are required')
            else:
                cursor.execute("select utype from employee where  name = %s AND password = %s ",(self.var_name.get(),self.var_pass.get()))
                login = cursor.fetchone()
                if login == None:
                    MessageBox.showerror('Error','Invalid Username/Password\n OR \nmight be you are not admin')
                else:
                    if login[0] == "Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
                        
                        
        except Exception as ex:
            MessageBox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def forget(self):
        con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
        cursor = con.cursor()
        try:
            if self.var_name.get() == "":
                MessageBox.showerror('Error','User must be having registered')
    
            else:
                cursor.execute("select email from employee where  name = %s ",(self.var_name.get(),))
                email = cursor.fetchone()
                if email == None:
                    MessageBox.showerror('Error','Invalid Employee ID,Try Again')
                else:
                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_cfn_pass = StringVar()
                    chk = self.send_email(email[0])
                    if chk != 's':
                        MessageBox.showerror("Error","Connection Error,try again",parent=self.root)
                    else:
                        self.forget_window=Toplevel(self.root)
                        self.forget_window.title('Reset Password')
                        self.forget_window.geometry('400x350+500+100')
                        self.forget_window.focus_force()

                        title = Label(self.forget_window,text='Reset Password',font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)

                        lbl_reset = Label(self.forget_window,text='Enter OTP Sent on registered E-mail',font=("times new roman",12)).place(x=20,y=60)
                        txt_reset = Entry(self.forget_window,textvariable=self.var_otp,font=("times new roman",12),bg='#d4d4d4').place(x=20,y=100,width=250,height=26)

                        self.btn_reset = Button(self.forget_window,text="Submit",font=("times new roman",12),command=self.validate_otp,bg='#3c4491',fg="white")
                        self.btn_reset.place(x=280,y=100,width=100,height=26)

                        lbl_pass = Label(self.forget_window,text='Enter New Password',font=("times new roman",12)).place(x=20,y=160)
                        txt_pass = Entry(self.forget_window,textvariable=self.var_new_pass,font=("times new roman",12),bg='#d4d4d4').place(x=20,y=190,width=250,height=26)

                        lbl_cfn_pass = Label(self.forget_window,text='Enter Confirm Password',font=("times new roman",12)).place(x=20,y=225)
                        txt_cfn_pass = Entry(self.forget_window,textvariable=self.var_cfn_pass,font=("times new roman",12),bg='#d4d4d4').place(x=20,y=255,width=250,height=26)

                        self.btn_update = Button(self.forget_window,text="Update",font=("times new roman",12),command=self.update_password,state=DISABLED,bg='#3c4491',fg="white")
                        self.btn_update.place(x=150,y=300,width=100,height=26)
                   

        except Exception as ex:
            MessageBox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    
    def update_password(self):
        if self.var_new_pass.get() == "" or self.var_cfn_pass.get() == "":
            MessageBox.showerror("Error","Password is required",parent=self.forget_window)
        elif self.var_new_pass.get() != self.var_cfn_pass.get():
            MessageBox.showerror("Error","Password should be same",parent=self.forget_window)
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
            cursor = con.cursor()
            # try:
            cursor.execute("Update employee password=%s where name = %s",(self.var_new_pass.get(),self.var_name.get()))
            con.commit()
            # except Exception as ex:
                # MessageBox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
                
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            MessageBox.showerror("Error","Invalid OTP,Try Again",parent=self.forget_window)
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        
        s.login(email_,pass_)
        
        self.otp=str(time.strftime("%H%M%S"))+str(time.strftime("%S"))

        subj = 'JI - Reset Password OTP'
        msg = f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nJI Team'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        
        chk = s.ehlo()
        if chk[0] == 250:
            return 's'
        else:
            return 'f'
                           

root = Tk()
obj = loginSystem(root)
root.mainloop()