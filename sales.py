from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import os 

class salesClass:
    def __init__(self, root):
        self.root = root 
        product_Frame = root
        product_Frame.geometry("1100x500+220+130")
        product_Frame.title("Stock Management System | Developed by JI")
        product_Frame.config(bg="white")
        product_Frame.focus_force()

        self.bill_list = []
        #==== VARIABLES ====
        self.var_invoice=StringVar()

        # ==== Title ====
        lbl_title = Label(self.root,text="View Customer Bill",font=("goudy old style",25),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10) 
        
        lbl_invoice = Label(self.root,text="Invoice No.",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_invoice = Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="#d4d4d4").place(x=160,y=100,width=180,height=25)

        btn_search=Button(self.root,text="Search",font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=360,y=100,width=120,height=25)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2",command=self.clear).place(x=490,y=100,width=120,height=25)
        
        # ==== Bill List ====
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)

        scrolly = Scrollbar(sales_frame,orient=VERTICAL)
        self.Sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)
        
        # ==== Bill Area ====
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)
        
        lbl_title = Label(bill_frame,text="Customer Bill Area",font=("goudy old style",18,"bold"),bg="lightgreen",fg="white").pack(side=TOP,fill=X) 

        scroll2 = Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=("goudy old style",15),bg="#d4d4d4",yscrollcommand=scroll2.set)
        scroll2.pack(side=RIGHT,fill=Y)
        scroll2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)
        
        # ==== Image ====
        self.bill_photo = Image.open("images/cat2.jpg")
        self.bill_photo=self.bill_photo.resize((450,300),Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image = Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=700,y=110)
        
        self.show()
    # ==== Fetching Bills ====
    def show (self):
        self.bill_list[:]
        self.Sales_list.delete(0,END)
        # print(os.listdir('bill'))
        for i in os.listdir('bill'):
            # print(i.split('.'),i.split)('0',[-1]]))
            if i.split('.')[-1] == 'txt':
                self.Sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
                
    def get_data (self,ev):
        index_ = self.Sales_list.curselection()
        file_name = self.Sales_list.get(index_)
        # print(file_name)
        self.bill_area.delete('1.0',END)
        fp = open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        
        fp.close()    
        
    def search (self):
        if self.var_invoice.get()=="":
            MessageBox.showerror("Error","Invoice no. Should Be Required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                MessageBox.showerror("Error","Invalid Invoice No.",parent=self.root)        

    def clear(self):
       self.show()
       self.bill_area.delete('1.0',END) 

if __name__=="__main__":       
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
