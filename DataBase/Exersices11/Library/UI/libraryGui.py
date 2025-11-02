from tkinter import Tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from DAL.DatabaseManager import DAL
from DAL.BookModel import Book
#------------------------------------------------------------------------------------------------------------
class Library_Gui:


    def set_Form_Size(self,form,width,hight):

        w=width
        h=hight
        ws=self.root.winfo_screenwidth()
        hs=self.root.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        form.geometry('%dx%d+%d+%d'%(w,h,x,y))
#---------------------------------------------Main------------------------------------------------------------    
    def __init__(self):

        self.root=Tk()
        self.set_Form_Size(self.root,400,300)
        self.root.title('عملیات کتابخانه')
        self.root.iconbitmap('UI/Icon/python_icon.ico')
        self.label_selection=Label(master=self.root,text='لطفا عملیات مورد نظر خود را انتخاب کنید')
        self.label_selection.grid(row=0,column=1,columnspan=3,pady=10)

        self.label_register=Label(master=self.root,text='گزینه 1 : ثبت کتاب')
        self.label_register.grid(row=1,column=1,columnspan=3,pady=10)

        self.label_remove=Label(master=self.root,text='گزینه 2 : حذف کتاب')
        self.label_remove.grid(row=2,column=1,columnspan=3,pady=10)

        
        self.label_search=Label(master=self.root,text='گزینه 3 : جستجو کتاب')
        self.label_search.grid(row=3,column=1,columnspan=3,pady=10)

        self.label_showBook=Label(master=self.root,text='گزینه 4 : نمایش کتاب')
        self.label_showBook.grid(row=4,column=1,columnspan=3,pady=10)

        self.entNum=Entry(master=self.root)
        self.entNum.grid(row=5,column=1,columnspan=3,pady=10)

        self.select_Button = Button(self.root, text='ثبت عملیات', bd=2, bg='green')
        self.select_Button.grid(row=6,column=1,columnspan=3,pady=10 )
        self.select_Button.bind("<Button>",lambda event:self.select_Operation(event,self.entNum.get()))

        self.root.columnconfigure(2,weight=2)
        self.root.mainloop()
#-------------------------------------------selectOperation------------------------------------------------------     
    def select_Operation(self,event,entry):

        global str_Result 
        entry=int(entry)

        if entry==1:
                
            win = Toplevel(self.root)
            win.title('ثبت اطلاعات کتاب')
            win.iconbitmap("UI/Icon/python_icon.ico")
            self.set_Form_Size(win,300,200)
                
            label1=Label(master=win,text="کد کتاب",width=10)
            label1.grid(row=0,column=0,pady=4)
            entCode=Entry(master=win)
            entCode.grid(row=0,column=1,pady=4)

            label2=Label(master=win,text="عنوان کتاب",width=10)
            label2.grid(row=1,column=0,pady=4)
            entTitle=Entry(master=win)
            entTitle.grid(row=1,column=1,pady=4)

            label3=Label(master=win,text="نویسنده",width=10)
            label3.grid(row=2,column=0,pady=4)
            entAuthor=Entry(master=win)
            entAuthor.grid(row=2,column=1,pady=4)
                
            label4=Label(master=win,text="ناشر",width=10)
            label4.grid(row=3,column=0,pady=4)
            entPublisher=Entry(master=win)
            entPublisher.grid(row=3,column=1,pady=4)

            btnRgister=Button(master=win, text="ثبت اطلاعات", bd=2, bg='green',command=win.destroy)
            btnRgister.grid(row=4,column=1,columnspan=3,pady=10)
            btnRgister.bind("<Button>",lambda event:self.insert_Book(event,entCode.get(),entTitle.get(),entAuthor.get(),entPublisher.get()))
                
            win.mainloop()

        elif entry==2:

            win = Toplevel(self.root)
            win.title('حذف کتاب')
            win.iconbitmap("UI/Icon/python_icon.ico")
            self.set_Form_Size(win,300,100)
                
            label1=Label(master=win,text=" کد کتاب  ",width=10)
            label1.grid(row=0,column=0,pady=4)
            entCode=Entry(master=win)
            entCode.grid(row=0,column=1,pady=4)

            btnDelete=Button(master=win, text="حذف کتاب", bd=2, bg='green')
            btnDelete.grid(row=1,column=1,columnspan=3,pady=10)
            btnDelete.bind("<Button>",lambda event:self.delete_Book(event,entCode.get()))
                
            win.mainloop()

        elif entry==3:

            win = Toplevel(self.root)
            win.title('جستجو کتاب')
            win.iconbitmap("UI/Icon/python_icon.ico")
            self.set_Form_Size(win,300,200)
                
            label1=Label(master=win,text=" کد کتاب  ",width=10)
            label1.grid(row=0,column=0,pady=4)
            entCode=Entry(master=win)
            entCode.grid(row=0,column=1,pady=4)

            btnSearch=Button(master=win, text="جستجو کتاب", bd=2, bg='green')
            btnSearch.grid(row=1,column=1,columnspan=3,pady=10)
            btnSearch.bind("<Button>",lambda event:self.search_Book(event,entCode.get()))
  
            str_Result= StringVar()
            msg1 = Message(master=win, textvariable=str_Result, width=100,fg='black',justify='center')  
            msg1.grid(row=2,column=1,columnspan=3) 

            win.mainloop()
           
        elif entry==4:

            win = Toplevel(self.root)
            win.title("فهرست کتاب ")
            win.iconbitmap("UI/Icon/python_icon.ico")
            self.set_Form_Size(win,800,300)

            tree = ttk.Treeview(win, column=("bookcode", "title", "author","publisher"), show='headings', height=10)
            tree.grid(row=1, columnspan=1)
            tree.column("#1", anchor=CENTER, width=50)
            tree.heading("#1", text="کد کتاب")
            tree.column("#2", anchor=CENTER, width=350)
            tree.heading("#2", text="نام کتاب")
            tree.column("#3", anchor=CENTER, width=250)
            tree.heading("#3", text="نویسنده")
            tree.column("#4", anchor=CENTER, width=100)
            tree.heading("#4", text="ناشر")

            db=DAL()
            books=db.showBooks()
            i=0
            for book in books:
                tree.insert('', 'end', text=str(i), values=(book[1],book[2],book[3],book[4]))
            i+=1

            tree.columnconfigure(0, weight=1)
            tree.pack()
            
            win.mainloop()
        
        else:
            
            messagebox.showerror('خطا','انتخاب گزینه نادرست')
            
#------------------------------------------insertBook--------------------------------------------------------
    def insert_Book(self,event,bookcode,title,author,publisher):
        
        try:
            book=Book(bookcode,title,author,publisher)
            db=DAL()
            result=db.insertBook(book)
            
            if result is True:
                messagebox.showinfo('درج','ثبت اطلاعات با موفقیت انجام شد') 

            else:
                messagebox.showwarning('هشدار',' فیلد کد کتاب خالی/تکراری است') 

        except:
                messagebox.showerror('خطا','خطا در ثبت اطلاعات ')

#-----------------------------------------deleteBook----------------------------------------------------------
    def delete_Book(self,event,bookcode):
            
        try:
            db=DAL()
            result=db.deleteBook(bookcode)
            
            if result is True:
                messagebox.showinfo('حذف','حذف کتاب با موفقیت انجام شد')   
            else:
                messagebox.showwarning('هشدار','کد کتاب یافت نشد ')
        except:
            messagebox.showerror('خطا','خطا در حذف کتاب ')

#--------------------------------------------searchBook-------------------------------------------------------
    def search_Book(self,event,bookcode):

        try:
            db=DAL()
            book=db.searchBook(bookcode)
            str_Result.set(book[2])    

        except:
            str_Result.set('کتاب مورد نظر یافت نشد')
                                


            
               
                 


