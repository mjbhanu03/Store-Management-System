from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import time
import os
import tempfile


class BillingClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Stock Management System | Developed by JI")
        self.root.config(bg="white")
        self.cart_list = []
        self.chk_print = 0 
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

        # ==== Produt Frame ====
        
        ProductFrame1= Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        p_title = Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="green",fg="white").pack(side=TOP,fill=X)
        
        # ==== Product Search Frame ====
        self.var_search=StringVar()
        ProductFrame2= Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)
        
        lbl_search = Label(ProductFrame2,text="Search Product | By JI",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_search = Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45,height=22)
        txt_search = Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="#d4d4d4").place(x=128,y=47,width=150,height=22)
        btn_search = Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="lightgreen",cursor="hand2",command=self.search).place(x=285,y=45,width=100,height=25)
        btn_show_all = Button(ProductFrame2,text="Show All",font=("goudy old style",15,"bold"),bg="#083531",fg="white",cursor="hand2",command=self.display).place(x=285,y=10,width=100,height=25)

      # ==== Billing Details ====
        
        cart_frame = Frame(ProductFrame1,bd=3,relief=RIDGE)
        cart_frame.place(x=2,y=140,width=398,height=385)
        
        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.BillingTable = ttk.Treeview(cart_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.BillingTable.xview)
        scrolly.config(command=self.BillingTable.yview)
        
        self.BillingTable.heading("pid",text="Pro Id")        
        self.BillingTable.heading("name",text="Name")        
        self.BillingTable.heading("price",text="Price")        
        self.BillingTable.heading("qty",text="QTY")        
        self.BillingTable.heading("status",text="Status")        
       
        self.BillingTable["show"]="headings"
       
        self.BillingTable.column("pid",width=40)        
        self.BillingTable.column("name",width=100)        
        self.BillingTable.column("price",width=100)        
        self.BillingTable.column("qty",width=40)        
        self.BillingTable.column("status",width=90)        
        self.BillingTable.pack(fill=BOTH,expand=1)
        self.BillingTable.bind("<ButtonRelease-1>",self.updateField)
        lbl_note = Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the cart'",font=("goudy old style",10),bg="white",fg="red").pack(side=BOTTOM,fill=X)
        con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
        cursor = con.cursor()
        
        # ==== Customer Frame ====
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        customerFrame= Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customerFrame.place(x=420,y=110,width=530,height=70)
          
        c_title = Label(customerFrame,text="Customer Details ",font=("goudy old style",14),bg="lightgrey").pack(side=TOP,fill=X)
        lbl_name = Label(customerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35,height=22)
        txt_name = Entry(customerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="#d4d4d4").place(x=80,y=35,width=180,height=22)
             
        lbl_contact = Label(customerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35,height=22)
        txt_contact = Entry(customerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="#d4d4d4").place(x=380,y=35,width=140,height=22)
          
        # ==== Cal Cart Frame ====  
        Cal_Cart_Frame= Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

        # ==== Calculator Frame ==== 
        self.var_cal_input=StringVar()
        
        Cal_Cart= Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Cart.place(x=5,y=10,width=268,height=340)


        txt_cal_input = Entry(Cal_Cart,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7 = Button(Cal_Cart,text=7,font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8 = Button(Cal_Cart,text=8,font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9 = Button(Cal_Cart,text=9,font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum = Button(Cal_Cart,text="+",font=('arial',15,'bold'),command=lambda:self.get_input("+"),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
       
        btn_4 = Button(Cal_Cart,text=4,font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5 = Button(Cal_Cart,text=5,font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6 = Button(Cal_Cart,text=6,font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub = Button(Cal_Cart,text="-",font=('arial',15,'bold'),command=lambda:self.get_input("-"),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
       
        btn_1 = Button(Cal_Cart,text=1,font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2 = Button(Cal_Cart,text=2,font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3 = Button(Cal_Cart,text=3,font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul = Button(Cal_Cart,text="*",font=('arial',15,'bold'),command=lambda:self.get_input("*"),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
       
        btn_0 = Button(Cal_Cart,text=0,font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c = Button(Cal_Cart,text="c",font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eql = Button(Cal_Cart,text="=",font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div = Button(Cal_Cart,text="/",font=('arial',15,'bold'),command=lambda:self.get_input("/"),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)
       
       
        # ==== Cart Frame ====
        
        cart_frame = Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=4,width=245,height=340)
        self.cart_title = Label(cart_frame,text="Cart \t Total Product: [0]",font=("goudy old style",12),bg="lightgrey")
        self.cart_title.pack(side=TOP,fill=X)
        
        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("pid",text="Product Id")        
        self.CartTable.heading("name",text="Name")        
        self.CartTable.heading("price",text="Price")        
        self.CartTable.heading("qty",text="Qty")        
       
        self.CartTable["show"]="headings"
       
        self.CartTable.column("pid",width=40)        
        self.CartTable.column("name",width=90)        
        self.CartTable.column("price",width=90)        
        self.CartTable.column("qty",width=30)         
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.updateFieldCart)
       
        con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
        cursor = con.cursor()

        # ==== ADD Cart Widget Frame ====
        self.var_pid = StringVar() 
        self.var_pname = StringVar() 
        self.var_qty = StringVar() 
        self.var_status = StringVar() 
        self.var_price = StringVar() 
        self.var_stock = StringVar() 
        
        Add_cartWidgetsFrame= Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Add_cartWidgetsFrame.place(x=420,y=550,width=530,height=110)

        lbl_name = Label(Add_cartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_name = Entry(Add_cartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="#d4d4d4",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_price = Label(Add_cartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_price = Entry(Add_cartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="#d4d4d4",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_qty = Label(Add_cartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_qty = Entry(Add_cartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="#d4d4d4").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock = Label(Add_cartWidgetsFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        btn_clear = Button(Add_cartWidgetsFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2",command=self.clear_cart).place(x=180,y=70,width=150,height=30)
        btn_add_cart = Button(Add_cartWidgetsFrame,text="Add | Update",font=("times new roman",15,"bold"),bg="lightgreen",cursor="hand2",command=self.add_update_cart).place(x=340,y=70,width=180,height=30)
        
        # ==== Billing Area ====
        
        billFrame =Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=390,height=410)
        
        p_title = Label(billFrame,text="Customer Bill",font=("goudy old style",20,"bold"),bg="green",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area = Text(billFrame)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        # ==== Billing  Buttons ====
        
        billMenuFrame =Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=390,height=140)
        
        self.lbl_amnt = Label(billMenuFrame,text='Bill Amount\n [0]',font=("goudy old style",15,"bold"),bg="darkgreen",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)
        
        self.lbl_discounnt = Label(billMenuFrame,text='Discount\n [5%]',font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
        self.lbl_discounnt.place(x=124,y=5,width=120,height=70)
        
        self.lbl_net_pay = Label(billMenuFrame,text='Net Pay\n [0]',font=("goudy old style",15,"bold"),bg="darkgreen",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=150,height=70)
        
        
        btn_print = Button(billMenuFrame,text='Print',font=("goudy old style",15,"bold"),cursor="hand2",bd=2,bg="darkgreen",fg="white",command=self.print_bill)
        btn_print.place(x=2,y=80,width=117,height=50)
        
        btn_clear_all = Button(billMenuFrame,text='Clear All',font=("goudy old style",15,"bold"),command=self.clear_all,cursor="hand2",bd=2,bg="lightgreen",fg="white")
        btn_clear_all.place(x=124,y=80,width=117,height=50)
        
        btn_generate = Button(billMenuFrame,text='Generate Bill',font=("goudy old style",15,"bold"),command=self.generate_bill,cursor="hand2",bd=2,bg="darkgreen",fg="white")
        btn_generate.place(x=246,y=80,width=148,height=50)
        
        # ==== Foorter ====
        
        footer = Label(self.root,text="SMS - Stock Management System | Developed by JI\nFor any technical issue contact: 7016 515 225",font=("times new roman",11),bg="#4d636d",fg="white",bd=0).pack(side=BOTTOM,fill=X) 
        self.display()
        self.update_date_time()
        
        
        # ==== All Functions ====
        
    def get_input(self,num):
        xnum = self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
      self.var_cal_input.set('')
      
    def perform_cal(self):
      result = self.var_cal_input.get()
      self.var_cal_input.set(eval(result))

    def display (self):
      # self.BillingTable = ttk.Treeview(cart_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
      con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
      cursor = con.cursor()
      for row in self.BillingTable.get_children():
          self.BillingTable.delete(row)
      
      cursor.execute("SELECT id,name,price,quantity,status FROM product WHERE status='Active'")
      
      rows = cursor.fetchall()

      for row in rows:
          self.BillingTable.insert("", "end", values=row)
          
      con.close()
      cursor.close()

    def search(self):
      con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
      cursor = con.cursor()
      try:
         
          if self.var_search.get()=="":
            MessageBox.showerror("Error","Search input should be required")
          else:
              # Add space before LIKE
            cursor.execute("select id,name,price,quantity,status from product where name LIKE '%" + self.var_search.get() + "%'and status='Active'")

            rows = cursor.fetchall()
            if len(rows) != 0:
              self.BillingTable.delete(*self.BillingTable.get_children())
              for row in rows:
                self.BillingTable.insert('', END, values=row)
            else:
                MessageBox.showerror("Error", "No record found", parent=self.root)

      except Exception as ex:
            MessageBox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def updateField(self,MJ):
      selected_items = self.BillingTable.focus()

      if not selected_items:
          MessageBox.showinfo("Error", "No item is selected for Update")
      else:
              con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
              cursor = con.cursor()
              # id,name,price,quantity,status
              values = self.BillingTable.item(selected_items, 'values')
              self.var_pid.set(values[0]) 
              self.var_pname.set(values[1]) 
              self.var_price.set(values[2]) 
              self.lbl_inStock.config(text=f"In Stock [{str(values[3])}]")
              self.var_stock.set(values[3])
              self.var_qty.set('1')

      con.close()
      cursor.close()


    def updateFieldCart(self,MJ):
      selected_items = self.CartTable.focus()

      if not selected_items:
          MessageBox.showinfo("Error", "No item is selected for Update")
      else:
              con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
              cursor = con.cursor()
              # id,name,price,quantity,status
              values = self.CartTable.item(selected_items, 'values')
              self.var_pid.set(values[0]) 
              self.var_pname.set(values[1]) 
              self.var_price.set(values[2]) 
              self.lbl_inStock.config(text=f"In Stock [{str(values[3])}]")
              self.var_stock.set(values[3])

              con.close()
              cursor.close()

    def add_update_cart(self):
      if self.var_pid.get() == '':
        MessageBox.showerror("Error","Please Select Any Product",parent=self.root)
        
      elif self.var_qty.get() == '' :
        MessageBox.showerror("Error","Quantity is Required",parent=self.root)
      
      elif int(self.var_qty.get()) > int(self.var_stock.get()):
        MessageBox.showerror("Error","Invalid Quantity",parent=self.root)
      
      else:
        # price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
        cart_data=[self.var_pid.get(),self.var_pname.get(),self.var_price.get(),self.var_qty.get(),self.var_stock.get()]
        price_cal = self.var_price.get()
        # ==== Update Cart ====
        present='no'
        index_=0
        for row in self.cart_list:
          if self.var_pid.get()==row[0]:
            present="yes"
            break
          
          index_+=1
        if present=='yes':
          op=MessageBox.askyesno('confirm',"product is already in the cart\nDo you want to update quantity | Remove from the cart",parent=self.root)
          if op==True:
            if self.var_qty.get()=="0":
              self.cart_list.pop(index_)
            else:
              # id,name,price,quantity,stock
              # self.cart_list[index_][2] =price_cal #price
              self.cart_list[index_][3] =self.var_qty.get() #qty
        
        else:      
          self.cart_list.append(cart_data)
        
        self.show_cart()
        self.bill_update()

    def bill_update(self):
      self.bill_amt=0
      self.net_pay=0
      self.discount = 0
      for row in self.cart_list:
      # id,name,price,quantity,status
        self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
      
      self.discount = (self.bill_amt*5)/100
      self.net_pay=self.bill_amt-self.discount
     
      self.lbl_amnt.config(text=f'Bill Amnt\n{str(self.bill_amt)}')
      self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
      self.cart_title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")      
      
    def show_cart(self):
      try:
          self.CartTable.delete(*self.CartTable.get_children())
          for row in self.cart_list:
            self.CartTable.insert('',END,values=row)
      
      except Exception as ex:
        MessageBox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def generate_bill(self):
      if self.var_cname.get() == "" or self.var_contact.get() == "":
        MessageBox.showerror("Error",f"Customer Details Are Required",parent=self.root)
      elif len(self.cart_list) == 0:
        MessageBox.showerror("Error",f"Please Add Product To The Cart!!!",parent=self.root)
      else:
        # ==== Bill Top ====
        self.bill_top()
        # ==== Bill Middle ====
        self.bill_middle()
        # ==== Bill Bottom====
        self.bill_bottom()
        fp = open(f'bill/{str(self.invoice)}.txt','w')
        fp.write(self.txt_bill_area.get('1.0',END))
        fp.close()
        MessageBox.showinfo('saved','Bill has been Generated/Saved in Backend',parent=self.root)
        self.chk_print = 1   
        pass  
    def bill_top(self):
      self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%M%S"))
      bill_top_temp= f'''
\t\tJI Store - Inventory
\tPhone No.7016515225 , Jamnagar-361005
{str("="*45)}
Customer Name: {self.var_cname.get()}      
Ph No.: {self.var_contact.get()}      
Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%y"))}      
{str("="*45)}      
Product Name\t\t\tQTY\tPrice
{str("="*45)}      
      '''
      self.txt_bill_area.delete('1.0',END)
      self.txt_bill_area.insert('1.0',bill_top_temp)
      
    def bill_bottom(self):
      bill_bottom_temp=f'''
{str("="*45)}
Bill Amount\t\t\t\tRs.{self.bill_amt}
Discount\t\t\t\tRs.{self.discount}
Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*45)}\n
      '''
      self.txt_bill_area.insert(END,bill_bottom_temp)

    def bill_middle(self):
      con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
      cursor = con.cursor()
      # try:
      # id,name,price,quantity,stock
      for row in self.cart_list:
          id = row[0]
          name=row[1]
          qty=int(row[4])-int(row[3])
          if int(row[3]) == int(row[4]):
              status = 'Inactive'
          if int(row[3]) != int(row[4]):
              status = 'Active'
              
          price=float(row[2])*int(row[3])
          price=str(price)
          self.txt_bill_area.insert(END,"\n"+name+"\t\t\t"+row[3]+"\tRs."+price)
          cursor.execute('update product set quantity=%s,status=%s WHERE id=%s',(qty, status, id))
          con.commit()
      con.close()
      self.display()    
      # except Exception as ex:
        # MessageBox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    
    def clear_cart(self):
      self.var_pid.set('') 
      self.var_pname.set('') 
      self.var_price.set('') 
      self.var_qty.set('') 
      self.lbl_inStock.config(text=f"In Stock")
      self.var_stock.set('')
  
    def clear_all(self):
      del self.cart_list[:]
      self.var_cname.set('')
      self.var_contact.set('')
      self.txt_bill_area.delete('1.0',END)
      self.cart_title.config(text=f"Cart \t Total Product: [0]")    
      self.var_search.set('')  
      self.clear_cart()
      self.display()
      self.show_cart()
      self.chk_print = 0
      
    def update_date_time(self):
      time_ = time.strftime("%I:%M:%S")
      date_ = time.strftime("%d-%m-%y")
      self.lbl_clock.config(text=f"Welcome to Stock Management System\t\t Date: {str(date_)} \t\t Time: {str(time_)}")
      self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
      if self.chk_print == 1:
        MessageBox.showinfo('Print',"Please wait while printing",parent=self.root)
        new_file = tempfile.mktemp('.txt')
        open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
        os.startfile(new_file,'print')

      else:
        MessageBox.showerror('Error',"Please generate bill, to print the receipt",parent=self.root)


    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":   
      
    root = Tk()
    obj = BillingClass(root)
    root.mainloop()
