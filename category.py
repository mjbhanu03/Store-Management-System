from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Stock Management System | Developed by JI")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ==== Variables ====
        self.var_catid = StringVar()
        self.var_name = StringVar()
        
        
        # ==== Title ====
        lbl_title = Label(self.root,text="Manage Product Category",font=("goudy old style",25),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10) 

        lbl_name = Label(self.root,text="Enter Category Name",font=("goudy old style",20),bg="white").place(x=50,y=100) 
        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="#d4d4d4").place(x=50,y=150,width=300,height=30) 
        
        # ==== Category Details ====
        
        cat_frame = Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(cat_frame,columns=("c_id","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        
        self.categoryTable.heading("c_id",text="Category ID")        
        self.categoryTable.heading("name",text="Name")        
        self.categoryTable["show"]="headings"
       
        self.categoryTable.column("c_id",width=90)        
        self.categoryTable.column("name",width=100)        

        self.categoryTable.pack(fill=BOTH,expand=1)
        con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
        cursor = con.cursor()
            
        
        # ==== Showing Data in TreeView
        def display ():
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor = con.cursor()
            
            for row in self.categoryTable.get_children():
                self.categoryTable.delete(row)
            
            cursor.execute("SELECT * FROM category")
            
            rows = cursor.fetchall()

            for row in rows:
                self.categoryTable.insert("", "end", values=row)
                
        display()
        cursor.close()
        con.close()
        
        # ==== Images Section ====
        
        self.im1 = Image.open("images/mob1.png")
        self.im1 = self.im1.resize((500,250),Image.LANCZOS)
        self.im1 = ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1 = Label(self.root,image=self.im1,bg="white")
        self.lbl_im1.place(x=50,y=220)

        self.im2 = Image.open("images/mob2.png")
        self.im2 = self.im2.resize((240,250),Image.LANCZOS)
        self.im2 = ImageTk.PhotoImage(self.im2)
        
        self.lbl_im2 = Label(self.root,image=self.im2,bg="white")
        self.lbl_im2.place(x=700,y=220)
        
        # ==== Insert ====
        def insert ():
            name = self.var_name.get();

            if(  name == ""):
                MessageBox.showinfo("Error","Please Insert All Details");
            else:
                con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
                cursor = con.cursor()
                cursor.execute("INSERT INTO category (name) VALUES (%s)",
               (name,))
                cursor.execute("commit");

                MessageBox.showinfo("Insert Status","Data Inserted");
                display()
       
        # ==== Delete ====   
       
        def delete ():
            con = mysql.connect(host="localhost",user="root",password="",database="stockmanagement")
            cursor=con.cursor()
            # cursor.execute("delete from employee where id='"+id+"'")
            # cursor.execute("commit")
            selected_items = self.categoryTable.selection()
            
            if not selected_items:
                MessageBox.showinfo("Error","No item selected for deletion")
                return 
            for item in selected_items:
                values = self.categoryTable.item(item,'values')
                
                c_id = values[0]
                
                cursor.execute("DELETE FROM category WHERE c_id=%s",(c_id,))
                
                con.commit()
                
                self.categoryTable.delete(item)
                
                MessageBox.showinfo("Delete Status","Selected record deleted successfully")

  

        btn_add = Button(self.root,text="Add",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2",command=insert).place(x=360,y=150,width=130,height=30)  
        btn_delete = Button(self.root,text="Delete",font=("goudy old style",15),bg="red",fg="white",cursor="hand2",command=delete).place(x=501,y=150,width=130,height=30) 



if __name__=="__main__":       
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
