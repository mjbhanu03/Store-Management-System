from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillingClass 
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import os
import time


class dashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Store Management System | Developed by JI")
        self.root.config(bg="white")

        # title
        self.icon_title = PhotoImage(file="images/logo.png")  # Correct file path
        title = Label(self.root, text="Stock Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 26, "bold"), bg="green", fg="white", anchor="w", padx="20")
        title.place(x=0, y=0, relwidth=1, height=55)  # Corrected placement
          # Corrected placement

        # btn_logout
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"),bg="white",fg="black",cursor="hand2",command=self.logout).place(x=1150,y=10,height=40,width=150)

        #===CLOCK===
        self.lbl_clock = Label(self.root, text="Welcome to Stock Management System\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",
                      font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=50, relwidth=1, height=30)  # Corrected placement
        
        #===Left Menu===
        self.MenuLogo = Image.open("images/leftmenu.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=85,width=200,height=550)
        
        lbl_menuLogo = Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        self.icon_side = PhotoImage(file="images/arrow.png")  # Correct file path
        self.phone_image = PhotoImage(file="images/iphone15.png")
        
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20),bg="#009688",fg="white").pack(side=TOP,fill=X)
        btn_bill = Button(LeftMenu, text="Bill", image=self.icon_side,command=self.bill,compound=RIGHT,anchor=W,padx=5,font=("times new roman", 20, "bold"),bg="white",fg="black",cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier",command=self.supplier, image=self.icon_side,compound=RIGHT,anchor=W,padx=5,font=("times new roman", 20, "bold"),bg="white",fg="black",cursor="hand2").pack(side=TOP,fill=X)
        btn_employee = Button(LeftMenu, text="Employee",command=self.employee, image=self.icon_side,compound=RIGHT,anchor=W,padx=5,font=("times new roman", 20, "bold"),bg="white",fg="black",cursor="hand2").pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu, text="Category",command=self.category, image=self.icon_side,compound=RIGHT,anchor=W,padx=5,font=("times new roman", 20, "bold"),bg="white",fg="black",cursor="hand2").pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu, text="Product",command=self.product, image=self.icon_side,compound=RIGHT,anchor=W,padx=5,font=("times new roman", 20, "bold"),bg="white",fg="black",cursor="hand2").pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu, text="Sales",command=self.sales, image=self.icon_side,compound=RIGHT,anchor=W,padx=5,font=("times new roman", 20, "bold"),bg="white",fg="black",cursor="hand2").pack(side=TOP,fill=X)
        # btn_exit = Button(LeftMenu, text="Exit", image=self.icon_side,compound=RIGHT,anchor=W,padx=5,font=("times new roman", 20, "bold"),bg="white",fg="black",cursor="hand2").pack(side=TOP,fill=X)
           
         # ====Content====             
        self.lbl_supplier = Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="white",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=700,y=107,height=150,width=300)
             
        self.lbl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#39c72c",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=1100,y=107,height=150,width=300)
             
        self.lbl_category = Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#39c72c",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=300,y=300,height=150,width=300)
             
        self.lbl_product = Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="white",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=700,y=300,height=150,width=300)
             
        self.lbl_sales = Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#39c72c",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=300,y=107,height=150,width=300)
             
        #===footer===
        self.lbl_footer = Label(self.root, text="JI- Stock Management System | Developed by Jay & Iram\n For any Technical issue contact:7016 515 225",
                      font=("times new roman", 12), bg="#4d636d", fg="white")
        self.lbl_footer.pack(side=BOTTOM,fill=X)  # Corrected placement

        self.update_content()
#=============================================================================== 
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

#=============================================================================== 
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

#=============================================================================== 
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

#=============================================================================== 
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

#=============================================================================== 
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

#=============================================================================== 
    def bill(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BillingClass(self.new_win)
    
    def update_content(self):
        con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
        cursor = con.cursor()
        try:
            cursor.execute("select * from product")
            product= cursor.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]")

            cursor.execute("select * from supplier")
            supplier= cursor.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier\n[ {str(len(supplier))} ]")

            cursor.execute("select * from category")
            category= cursor.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(category))} ]")

            cursor.execute("select * from employee")
            employee= cursor.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")
       
            self.lbl_sales.config(text=f'Total Sales\n[ {str(len(os.listdir('bill')))} ]')
       
            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%y")
            self.lbl_clock.config(text=f"Welcome to Stock Management System\t\t Date: {str(date_)} \t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            MessageBox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")


if __name__== "__main__":       
    root = Tk()
    obj = dashboard(root)
    root.mainloop()
