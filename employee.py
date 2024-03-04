from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import mysql.connector as mysql
from tkcalendar import DateEntry #pip install tkcalendar
import tkinter.messagebox as MessageBox

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Stock Management System | Developed by JI")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
        # =================================================
        # All Variables============
        self.var_searchBy = StringVar()
        self.var_searchText = StringVar()
        
        
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        self.var_id = StringVar()
        self.var_searchBy = StringVar()
        self.var_searchText = StringVar()
        
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
                    cursor.execute("select * from employee where "+self.var_searchBy.get() + " LIKE '%" + self.var_searchText.get() + "%'")

                    rows = cursor.fetchall()
                    if len(rows) != 0:
                        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                        for row in rows:
                            self.EmployeeTable.insert('', END, values=row)
                    else:
                        MessageBox.showerror("Error", "No record found", parent=self.root)

            except Exception as ex:
                MessageBox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



        # ====searchframe====
        SearchFrame = LabelFrame(self.root,text="Search Employee",font=("goudy old style",15,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        # ====options====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchBy,values=("Select","Emails","Name","Employee ID","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame,textvariable=self.var_searchText,font=("goudy old style",15),bg="#d4d4d4").place(x=200,y=10)
        btn_search = Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=search).place(x=410,y=9,width=150,height=30)

        #===title===
        title= Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        # ===Content===
        # ===Row 1===
        lbl_empGender= Label(self.root,text="Gender",font=("goudy old style",12),bg="white").place(x=350,y=150)
        lbl_empContact= Label(self.root,text="Contact",font=("goudy old style",12),bg="white").place(x=750,y=150)

        self.txt_empGender= Entry(self.root,textvariable=self.var_gender,font=("goudy old style",12),bg="white")
        self.txt_empGender.place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        
        self.txt_empContact= Entry(self.root,textvariable=self.var_contact,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_empContact.place(x=850,y=150,width=180)

        # ===Row 2===
        lbl_name= Label(self.root,text="Name",font=("goudy old style",12),bg="white").place(x=50,y=150)
        lbl_dob= Label(self.root,text="D.O.B",font=("goudy old style",12),bg="white").place(x=350,y=190)
        lbl_doj= Label(self.root,text="D.O.J",font=("goudy old style",12),bg="white").place(x=750,y=190)

        self.txt_name= Entry(self.root,textvariable=self.var_name,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_name.place(x=150,y=150,width=180)
        self.txt_dob= DateEntry(self.root,textvariable=self.var_dob,font=("goudy old style",12),bg="#d4d4d4",date_pattern="yyyy/mm/dd")
        self.txt_dob.place(x=500,y=190,width=180)
        self.txt_doj= DateEntry(self.root,textvariable=self.var_doj,font=("goudy old style",12),bg="#d4d4d4",date_pattern="yyyy/mm/dd")
        self.txt_doj.place(x=850,y=190,width=180)

        # ===Row 3===
        lbl_email= Label(self.root,text="Email",font=("goudy old style",12),bg="white").place(x=50,y=230)
        lbl_pass= Label(self.root,text="Password",font=("goudy old style",12),bg="white").place(x=350,y=230)
        lbl_utype= Label(self.root,text="User Type",font=("goudy old style",12),bg="white").place(x=50,y=190)

        self.txt_email= Entry(self.root,textvariable=self.var_email,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_email.place(x=150,y=230,width=180)
        self.txt_pass= Entry(self.root,textvariable=self.var_pass,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_pass.place(x=500,y=230,width=180)
        self.txt_utype= Entry(self.root,textvariable=self.var_utype,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_utype.place(x=150,y=190,width=180)

        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",12))
        cmb_utype.place(x=150,y=190,width=180)
        cmb_utype.current(0)
        
         # ===Row 4===
        lbl_add= Label(self.root,text="Address",font=("goudy old style",12),bg="white").place(x=50,y=270)
        lbl_salary= Label(self.root,text="Salary",font=("goudy old style",12),bg="white").place(x=750,y=230)

        self.txt_add= Text(self.root,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_add.place(x=150,y=270,width=300,height=60)
        self.txt_salary= Entry(self.root,textvariable=self.var_salary,font=("goudy old style",12),bg="#d4d4d4")
        self.txt_salary.place(x=850,y=230,width=180)
        
        # ==== Insert Part ===
        def insert ():
            name = self.txt_name.get()
            gender = self.txt_empGender.get()
            contact = self.txt_empContact.get()
            dob = self.txt_dob.get()
            doj = self.txt_doj.get()
            email = self.txt_email.get()
            password = self.txt_pass.get()
            utype = self.txt_utype.get()
            address  = self.txt_add.get("1.0", "end-1c")
            salary = self.txt_salary.get()


            if( name == "" or gender == "" or contact == "" or dob == "" or doj == "" or email == "" or  password == "" or  utype == "" or address == "" or  salary == ""):
                MessageBox.showinfo("Error","Please Insert All Details");
            else:
                con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
                cursor = con.cursor()
                cursor.execute("INSERT INTO employee (name, contact, gender, dob, doj, email, password, utype, address, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               (name, contact, gender, dob, doj, email, password, utype, address, salary))
                cursor.execute("commit");

                MessageBox.showinfo("Insert Status","Data Inserted");
                display()
                
        # ===== DELETE SECTION =====
        def delete ():
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor=con.cursor()
            # cursor.execute("delete from employee where id='"+id+"'")
            # cursor.execute("commit")
            selected_items = self.EmployeeTable.selection()
            
            if not selected_items:
                MessageBox.showinfo("Error","No item selected for deletion")
                return 
            for item in selected_items:
                values = self.EmployeeTable.item(item,'values')
                
                id = values[0]
                
                cursor.execute("DELETE FROM employee WHERE id=%s",(id,))
                
                con.commit()
                
                self.EmployeeTable.delete(item)
                
                MessageBox.showinfo("Delete Status","Selected record deleted successfully")

                
        # ==== GET CONTENT CODE ====      
        def updateField():
            selected_items = self.EmployeeTable.focus()

            if not selected_items:
                MessageBox.showinfo("Error", "No item selected for Update")
            else:
                try:
                    con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
                    cursor = con.cursor()

                    values = self.EmployeeTable.item(selected_items, 'values')
                    id = values[0]
                    self.var_id.set(id)
                    self.txt_name.delete(0, END)
                    self.txt_name.insert(0, values[1])
                    self.txt_empContact.delete(0, END)
                    self.txt_empContact.insert(0, values[4])
                    self.txt_empGender.delete(0, END)
                    self.txt_empGender.insert(0, values[3])
                    self.txt_dob.delete(0, END)
                    self.txt_dob.insert(0, values[5])
                    self.txt_doj.delete(0, END)
                    self.txt_doj.insert(0, values[6])
                    self.txt_email.delete(0, END)
                    self.txt_email.insert(0, values[2])
                    self.txt_pass.delete(0, END)
                    self.txt_pass.insert(0, values[7])
                    self.txt_utype.delete(0, END)
                    self.txt_utype.insert(0, values[8])
                    self.txt_add.delete(1.0, END)
                    self.txt_add.insert(1.0, values[9])
                    self.txt_salary.delete(0, END)
                    self.txt_salary.insert(0, values[10])
                    
                except BaseException as err:
                    print("error==>",err)
                    MessageBox.showerror("Error", f"Error: {err}")
                finally:
                    cursor.close()
                    con.close()
                    
        # updateEmployee()  
        def updateEmployee():
            selected_items = self.EmployeeTable.focus()

            if not selected_items:
                MessageBox.showinfo("Error", "No item selected for Update")
            else:
                con = mysql.connect(host="localhost", user="root", password="", database="stockmanagement")
                cursor = con.cursor()
                name = self.txt_name.get()
                gender = self.txt_empGender.get()
                contact = self.txt_empContact.get()
                dob = self.txt_dob.get()
                doj = self.txt_doj.get()
                email = self.txt_email.get()
                password = self.txt_pass.get()
                utype = self.txt_utype.get()
                address = self.txt_add.get("1.0", "end-1c")
                id = self.var_id.get()

                salary = self.txt_salary.get()
                
                cursor.execute("UPDATE employee SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, doj=%s, password=%s,utype=%s, address=%s, salary=%s WHERE id=%s",
                               ( name, email, gender, contact, dob, doj, password, utype, address, salary, id))

                MessageBox.showinfo("Update Status", "Data Updated")
                con.commit()
                cursor.close()
                con.close()
                display()
        
        # ==== Clear All Fields ====
        def clear ():
            
            self.txt_name.delete(0, END)
            self.txt_empContact.delete(0, END)
            self.txt_empGender.delete(0, END)
            self.txt_dob.set_date(None)  # Clear DateEntry widget
            self.txt_doj.set_date(None)  # Clear DateEntry widget
            self.txt_email.delete(0, END)
            self.txt_pass.delete(0, END)
            self.txt_utype.delete(0, END)
            self.txt_add.delete("1.0", END)
            self.txt_salary.delete(0, END) 
            self.var_searchText.set("") 
            self.var_searchBy.set("") 
             

            
        # =====Buttons=====
        btn_add = Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white",cursor="hand2",command=insert).place(x=500,y=285,width=110,height=28)
        btn_get = Button(self.root,text="Get",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=updateField).place(x=650,y=285,width=55,height=28)
        btn_update = Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=updateEmployee).place(x=710,y=285,width=75,height=28)
        btn_delete = Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=delete).place(x=800,y=285,width=110,height=28)
        btn_clear = Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="white",cursor="hand2",command=clear).place(x=950,y=285,width=110,height=28)
        
        # ==== Employee Details ====
        
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame,columns=("id","name","email","gender","contact","dob","doj","password","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("id",text="Employee ID")        
        self.EmployeeTable.heading("name",text="Name")        
        self.EmployeeTable.heading("email",text="Email")        
        self.EmployeeTable.heading("gender",text="Gender")        
        self.EmployeeTable.heading("contact",text="Contact")        
        self.EmployeeTable.heading("dob",text="Date Of Birth")        
        self.EmployeeTable.heading("doj",text="Date Of Joining")        
        self.EmployeeTable.heading("password",text="Password")        
        self.EmployeeTable.heading("utype",text="User Type")        
        self.EmployeeTable.heading("address",text="Address")        
        self.EmployeeTable.heading("salary",text="Salary")        
       
        self.EmployeeTable["show"]="headings"
       
        self.EmployeeTable.column("id",width=90)        
        self.EmployeeTable.column("name",width=100)        
        self.EmployeeTable.column("email",width=100)        
        self.EmployeeTable.column("gender",width=100)        
        self.EmployeeTable.column("contact",width=100)        
        self.EmployeeTable.column("dob",width=100)        
        self.EmployeeTable.column("doj",width=100)        
        self.EmployeeTable.column("password",width=100)        
        self.EmployeeTable.column("utype",width=100)        
        self.EmployeeTable.column("address",width=100)        
        self.EmployeeTable.column("salary",width=100) 
       
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
        cursor = con.cursor()
        
        # ==== Showing Data in TreeView
        def display ():
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor = con.cursor()
            for row in self.EmployeeTable.get_children():
                self.EmployeeTable.delete(row)
            
            cursor.execute("SELECT id, name, email, gender, contact, dob, doj, password, utype, address, salary FROM employee")
            
            rows = cursor.fetchall()

            for row in rows:
                self.EmployeeTable.insert("", "end", values=row)
                
        display()
        cursor.close()
        con.close()
        
        # def close_window(self):
        #     # Close the window
        #     self.root.destroy()
        

if __name__=="__main__":       
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
