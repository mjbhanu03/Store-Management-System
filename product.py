from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

class productClass:
    def __init__(self, root):
        self.root = root 
        product_Frame = root
        product_Frame.geometry("1100x500+220+130")
        product_Frame.title("Stock Management System | Developed by JI")
        product_Frame.config(bg="white")
        product_Frame.focus_force()

        # Initialize variables
        self.var_id = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.cat_list= []
        self.sup_list = []

        # Call fetch_cat_sup
        self.fetch_cat_sup()

        self.var_searchBy = StringVar()
        self.var_searchText = StringVar()

        product_Frame = Frame(product_Frame,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        def search():
            con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
            cursor = con.cursor()
            try:
                if self.var_searchBy.get()=="Select":
                    MessageBox.showerror("Error","Select Search By Option")
                elif self.var_searchText.get()=="":
                    MessageBox.showerror("Error","Search input should be required")
                else:
                    # Add space before LIKE
                    cursor.execute("select * from product where "+self.var_searchBy.get() + " LIKE '%" + self.var_searchText.get() + "%'")

                    rows = cursor.fetchall()
                    if len(rows) != 0:
                        self.ProductTable.delete(*self.ProductTable.get_children())
                        for row in rows:
                            self.ProductTable.insert('', END, values=row)
                    else:
                        MessageBox.showerror("Error", "No record found", parent=self.root)

            except Exception as ex:
                MessageBox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

        #===title===
        title= Label(product_Frame,text="Products Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        # ==== Column 1 ====
        lbl_cat= Label(product_Frame,text="Category",font=("goudy old style",15),bg="white").place(x=30,y=60)
        lbl_supplier= Label(product_Frame,text="Supplier",font=("goudy old style",15),bg="white").place(x=30,y=110)
        lbl_product= Label(product_Frame,text="Name",font=("goudy old style",15),bg="white").place(x=30,y=160)
        lbl_price= Label(product_Frame,text="Price",font=("goudy old style",15),bg="white").place(x=30,y=210)
        lbl_qty= Label(product_Frame,text="Quantity",font=("goudy old style",15),bg="white").place(x=30,y=260)
        lbl_status= Label(product_Frame,text="Status",font=("goudy old style",15),bg="white").place(x=30,y=310)

        # ==== Column 2 ====
        self.cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",12))
        self.cmb_cat.place(x=150,y=60,width=200)
        self.cmb_cat.current(0)

        self.cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",12))
        self.cmb_sup.place(x=150,y=110,width=200)
        self.cmb_sup.current(0)

        self.text_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="#d4d4d4").place(x=150,y=160,width=200)
        self.text_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="#d4d4d4").place(x=150,y=210,width=200)
        self.text_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="#d4d4d4").place(x=150,y=260,width=200)

        self.cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",12))
        self.cmb_status.place(x=150,y=310,width=200)
        self.cmb_status.current(0)

        # ==== Fetching Data ====
        self.fetch_cat_sup()
        
        # Add Data
        def insert ():
            
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor = con.cursor()
            if(self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_sup.get() == "Select" or self.var_sup.get() == "Empty"):
                MessageBox.showinfo("Error","Please Insert All Details");
            else:
                cursor.execute("INSERT INTO product (category,supplier,name,price,quantity,status) VALUES (%s,%s, %s, %s, %s, %s)",
                (self.var_cat.get(),self.var_sup.get(),self.var_name.get(),self.var_price.get(),self.var_qty.get(),self.var_status.get()))
                cursor.execute("commit");

                MessageBox.showinfo("Insert Status","Data Inserted");
            display()
                

        def updateField():
            selected_items = self.ProductTable.focus()

            if not selected_items:
                MessageBox.showinfo("Error", "No item is selected for Update")
            else:
                try:
                    con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
                    cursor = con.cursor()

                    values = self.ProductTable.item(selected_items, 'values')
                    id = values[0]
                    self.var_id.set(id)
                    self.var_cat.set(values[1]),
                    self.var_sup.set(values[2]),
                    self.var_name.set(values[3]),
                    self.var_price.set(values[4]),
                    self.var_qty.set(values[5]),
                    self.var_status.set(values[6])
                    
                except BaseException as err:
                    print("error==>",err)
                    MessageBox.showerror("Error", f"Error: {err}")
                
                    cursor.close()
                    con.close()
                    
        def updateProduct():
            selected_items = self.ProductTable.focus()

            if not selected_items:
                MessageBox.showinfo("Error", "No item is selected for Update")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
                cursor = con.cursor()
                id = self.var_id.get()
                category = self.var_cat.get()
                supplier = self.var_sup.get()
                name = self.var_name.get()
                price = self.var_price.get()
                quantity = self.var_qty.get()
                status = self.var_status.get()

                
                cursor.execute("UPDATE product SET category=%s, supplier=%s, name=%s,price=%s, quantity=%s,status=%s WHERE id=%s",
                               (category, supplier, name, price, quantity, status, id))

                MessageBox.showinfo("Update Status", "Data Updated")
                con.commit()
                cursor.close()
                con.close()
                display()
                
        
        def delete ():
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor=con.cursor()
            # cursor.execute("delete from employee where id='"+id+"'")
            # cursor.execute("commit")
            selected_items = self.ProductTable.selection()
            
            if not selected_items:
                MessageBox.showinfo("Error","No item selected for deletion")
                return 
            for item in selected_items:
                values = self.ProductTable.item(item,'values')
                
                id = values[0]
                
                cursor.execute("DELETE FROM product WHERE id=%s",(id,))
                
                con.commit()
                
                self.ProductTable.delete(item)
                MessageBox.showinfo("Delete Status","Selected record deleted successfully")

        def display ():
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor = con.cursor()
            for row in self.ProductTable.get_children():
                self.ProductTable.delete(row)
            
            cursor.execute("SELECT id, category, supplier, name, price, quantity, status FROM product")
            
            rows = cursor.fetchall()

            for row in rows:
                self.ProductTable.insert("", "end", values=row)
                
            display()
            cursor.close()
            con.close()

        def clear ():  
            self.cmb_cat.set("Select")
            self.cmb_sup.set("Select")
            self.var_name.set("")
            self.var_price.set("")
            self.var_qty.set("") 
            self.cmb_status.set("Active")
            self.var_searchText.set("") 
            self.var_searchBy.set("") 
             



        # ==== Buttons ====
        btn_add = Button(product_Frame,text="Save",font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white",cursor="hand2",command=insert).place(x=10,y=400,width=90,height=30)
        btn_get = Button(product_Frame,text="Get",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=updateField).place(x=110,y=400,width=50,height=30)
        btn_update = Button(product_Frame,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=updateProduct).place(x=165,y=400,width=75,height=30)
        btn_delete = Button(product_Frame,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=delete).place(x=250,y=400,width=90,height=30)
        btn_clear = Button(product_Frame,text="Clear",font=("goudy old style",15,"bold"),bg="white",cursor="hand2",command=clear).place(x=350,y=400,width=90,height=30)

        # ==== Search Frame ====
        SearchFrame = LabelFrame(root, text="Search Employee", font=("goudy old style",15,"bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        # ==== Options ====
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchBy, values=("select","category","supplier","Name"), state='readonly', justify=CENTER, font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchText, font=("goudy old style",15), bg="#d4d4d4").place(x=200,y=10)
        btn_search = Button(SearchFrame, text="Search", font=("goudy old style",15), bg="#4caf50", fg="white", cursor="hand2",command=search).place(x=410,y=9,width=150,height=30)

        # ==== Product Details ====
        pro_frame = Frame(root, bd=3, relief=RIDGE)
        pro_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly = Scrollbar(pro_frame, orient=VERTICAL)
        scrollx = Scrollbar(pro_frame, orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(pro_frame, columns=("id","category","supplier","name","price","quantity","status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        
        self.ProductTable.heading("id", text="Product Id")        
        self.ProductTable.heading("category", text="Category")        
        self.ProductTable.heading("supplier", text="Supplier")        
        self.ProductTable.heading("name", text="Name")        
        self.ProductTable.heading("price", text="Price")        
        self.ProductTable.heading("quantity", text="Quantity")        
        self.ProductTable.heading("status", text="Status")        

        self.ProductTable["show"]="headings"
       
        self.ProductTable.column("id", width=90)        
        self.ProductTable.column("category", width=100)        
        self.ProductTable.column("supplier", width=100)        
        self.ProductTable.column("name", width=100)        
        self.ProductTable.column("price", width=100)        
        self.ProductTable.column("quantity", width=100)        
        self.ProductTable.column("status", width=100)        

        self.ProductTable.pack(fill=BOTH, expand=1)
        
        # Display data
        self.display()

    def fetch_cat_sup(self):
        con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
        cursor = con.cursor()            
        try:    
            self.cat_list.append("Empty")
            self.sup_list.append("Empty")
            cursor.execute("select name from category")
            cat= cursor.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
            for i in cat:
                self.cat_list.append(i[0])    
            # print(self.cat_list)

            cursor.execute("select name from supplier")
            sup = cursor.fetchall()
            
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
            for i in sup:
                self.sup_list.append(i[0])    
            # print(self.sup_list)

        except BaseException as err:
            print("error==>", err)
            MessageBox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()
            con.close()
            

    def display(self):
        con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
        cursor = con.cursor()
        for row in self.ProductTable.get_children():
            self.ProductTable.delete(row)
        
        cursor.execute("SELECT * FROM product")
        
        rows = cursor.fetchall()

        for row in rows:
            self.ProductTable.insert("", "end", values=row)
            
        cursor.close()
        con.close()

if __name__=="__main__":       
    root = Tk()
    obj = productClass(root)
    root.mainloop()
