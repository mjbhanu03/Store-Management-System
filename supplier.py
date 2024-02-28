from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Stock Management System | Developed by JI")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
        # =================================================
        # All Variables============
        self.var_searchText = StringVar()
        
        self.var_invoice_no = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_desc = StringVar()

        
        def search():
            con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
            cursor = con.cursor()
            try:
                if self.var_searchText.get()=="":
                    MessageBox.showerror("Error","Search input should be required")
                else:
                    # Add space before LIKE
                    cursor.execute("select * from supplier where invoice_no=%s", (self.var_searchText.get(),))
                    rows = cursor.fetchone()
                    if rows != None:
                        self.SupplierTable.delete(*self.SupplierTable.get_children())
                        self.SupplierTable.insert('', END, values=rows)
                    else:
                        MessageBox.showerror("Error", "No record found", parent=self.root)

            except Exception as ex:
                MessageBox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



        # ====Search Frame====
       
        # ====options====
        lbl_search=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white")
        lbl_search.place(x=700,y=80)
        
        txt_search = Entry(self.root,textvariable=self.var_searchText,font=("goudy old style",15),bg="#d4d4d4").place(x=800,y=80,height=28,width=160)
        btn_search = Button(self.root,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=search).place(x=980,y=79,width=100,height=28)

        #===title===
        title= Label(self.root,text="Supplier Details",font=("goudy old style",17,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)
        
        # ===Content===
        # ===Row 1===
        lbl_invno= Label(self.root,text="Invoice No.",font=("goudy old style",12),bg="white").place(x=50,y=60)
        lbl_name= Label(self.root,text="Name",font=("goudy old style",12),bg="white").place(x=50,y=110)

        self.txt_invno= Entry(self.root,textvariable=self.var_invoice_no,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_invno.place(x=150,y=60,width=180)

        self.txt_name= Entry(self.root,textvariable=self.var_name,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_name.place(x=150,y=110,width=180)

        # ===Row 3===
        lbl_contact= Label(self.root,text="Contact",font=("goudy old style",12),bg="white").place(x=50,y=160)

        self.txt_contact= Entry(self.root,textvariable=self.var_contact,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_contact.place(x=150,y=160,width=180)
        
         # ===Row 4===
        lbl_desc= Label(self.root,text="Description",font=("goudy old style",12),bg="white").place(x=50,y=210)

        self.txt_desc= Text(self.root,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_desc.place(x=150,y=210,width=500,height=90)
        
        # ==== Insert Part ===
        def insert ():
            invoice_no = self.txt_invno.get();
            name = self.txt_name.get();
            contact = self.txt_contact.get();
            description  = self.txt_desc.get("1.0", "end-1c");
            
            if(invoice_no == "" or name == "" or contact == "" or description == ""):
                MessageBox.showinfo("Error","Please Insert All Details");
            else:
                con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
                cursor = con.cursor()
                
                cursor.execute("select * from supplier where invoice_no = %s",(invoice_no,))
                existing_record = cursor.fetchone()

                if existing_record is not None:
                    new_invoice_no = generate_new_invoice_number(invoice_no)
                    self.txt_invno.delete(0,END)
                    self.txt_invno.insert(END,new_invoice_no)
                    invoice_no = new_invoice_no
                
                
                cursor.execute("INSERT INTO supplier (invoice_no,name,description, contact) VALUES (%s,%s, %s, %s)",
                (invoice_no,name,description,contact))
                cursor.execute("commit");

                MessageBox.showinfo("Insert Status","Data Inserted");
                display()
                
        def generate_new_invoice_number(existing_invoice_number):
            # Assuming your invoice numbers are numeric and sequential
            # You can modify this function based on your actual invoice numbering system
            # For example, you could append a suffix or increment the number
            new_invoice_number = int(existing_invoice_number) + 1
            return str(new_invoice_number)

                
        # ===== DELETE SECTION =====
        def delete ():
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor=con.cursor()
            # cursor.execute("delete from employee where id='"+id+"'")
            # cursor.execute("commit")
            selected_items = self.SupplierTable.selection()
            
            if not selected_items:
                MessageBox.showinfo("Error","No item selected for deletion")
                return 
            for item in selected_items:
                values = self.SupplierTable.item(item,'values')
                
                invoice_no = values[0]
                
                cursor.execute("DELETE FROM supplier WHERE invoice_no=%s",(invoice_no,))
                
                con.commit()
                
                self.SupplierTable.delete(item)
                
                MessageBox.showinfo("Delete Status","Selected record deleted successfully")

                
        # ==== GET CONTENT CODE ====      
        def updateField():
            selected_items = self.SupplierTable.focus()

            if not selected_items:
                MessageBox.showinfo("Error", "No item selected for Update")
            else:
                try:
                    con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
                    cursor = con.cursor()

                    values = self.SupplierTable.item(selected_items, 'values')
                    self.txt_invno.delete(0,END)
                    self.txt_invno.insert(0,values[0])
                    self.txt_name.delete(0, END)
                    self.txt_name.insert(0, values[1])
                    self.txt_desc.delete(1.0, END)
                    self.txt_desc.insert(1.0, values[2])
                    self.txt_contact.delete(0, END)
                    self.txt_contact.insert(0, values[3])

                    
                except BaseException as err:
                    print("error==>",err)
                    MessageBox.showerror("Error", f"Error: {err}")
                finally:
                    cursor.close()
                    con.close()
                    
        # updateSupplier()  
        def updateSupplier():
            selected_items = self.SupplierTable.focus()

            if not selected_items:
                MessageBox.showinfo("Error", "No item selected for Update")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
                cursor = con.cursor()
                name = self.txt_name.get()
                contact = self.txt_contact.get()
                description = self.txt_desc.get("1.0", "end-1c")
                invoice_no = self.txt_invno.get()

                
                cursor.execute("UPDATE supplier SET name=%s, contact=%s, description=%s WHERE invoice_no=%s",
                               (name, contact,description, invoice_no))

                MessageBox.showinfo("Update Status", "Data Updated")
                con.commit()
                cursor.close()
                con.close()
                display()
        
        # ==== Clear All Fields ====
        def clear ():
            
            self.txt_invno.delete(0, END)
            self.txt_name.delete(0, END)
            self.txt_contact.delete(0, END)
            self.txt_desc.delete("1.0", END)
            self.var_searchText.set("") 
             

            
        # =====Buttons=====
        btn_add = Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white",cursor="hand2",command=insert).place(x=150,y=325,width=110,height=28)
        btn_get = Button(self.root,text="Get",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=updateField).place(x=272,y=325,width=55,height=28)
        btn_update = Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=updateSupplier).place(x=328,y=325,width=75,height=28)
        btn_delete = Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=delete).place(x=416,y=325,width=110,height=28)
        btn_clear = Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="white",cursor="hand2",command=clear).place(x=540,y=325,width=110,height=28)
        
        # ==== Supplier Details ====
        
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frame,columns=("invoice_no","name","contact","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading("invoice_no",text="Invoice No.")        
        self.SupplierTable.heading("name",text="Name")        
        self.SupplierTable.heading("contact",text="Contact")        
        self.SupplierTable.heading("description",text="Description")        
       
        self.SupplierTable["show"]="headings"
       
        self.SupplierTable.column("invoice_no",width=90)        
        self.SupplierTable.column("name",width=100)        
        self.SupplierTable.column("contact",width=100)        
        self.SupplierTable.column("description",width=100)        
       
        self.SupplierTable.pack(fill=BOTH,expand=1)
        con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
        cursor = con.cursor()
        

            
        
        # ==== Showing Data in TreeView
        def display ():
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor = con.cursor()
            
            for row in self.SupplierTable.get_children():
                self.SupplierTable.delete(row)
            
            cursor.execute("SELECT * FROM supplier")
            
            rows = cursor.fetchall()

            for row in rows:
                self.SupplierTable.insert("", "end", values=row)
                
        display()
        cursor.close()
        con.close()
        
                # ==== SEARCH ====


if __name__=="__main__":       
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
