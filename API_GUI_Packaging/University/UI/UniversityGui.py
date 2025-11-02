from tkinter import *
from tkinter import ttk
from DAL.DatabaseManager import *
#----------------------------------------------------------------------------------------------------------------
class Gui:
    
    def set_Form_Size(self,form,width,height):
        w = width
        h = height
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2)-(w/2)
        y = (hs/2)-(h/2)
        form.geometry("%dx%d+%d+%d" %(w,h,x,y))
#----------------------------------------------------------------------------------------------------------------
    def __init__(self):

        self.root=Tk()
        self.set_Form_Size(self.root,300,200)
        self.root.title('جستجو دانشگاه')
        self.root.iconbitmap('UI/Icon/universitygraduatehat.ico')
        self.label_selection=Label(master=self.root,text='استان مورد نظر خود را وارد کنید')
        self.label_selection.grid(row=1,column=1,columnspan=3,pady=10)

        self.entState=Entry(master=self.root)
        self.entState.grid(row=3,column=1,columnspan=3,pady=10)

        self.show_Button = Button(self.root, text='نمایش', bd=2, bg='#138D75')
        self.show_Button.grid(row=5,column=1,columnspan=3,pady=10 )
        self.show_Button.bind("<Button>",lambda event:self.show_Information(event,self.entState.get()))
        self.show_Button.config(command=lambda: self.entState.delete(0,END))
     
        self.root.columnconfigure(2,weight=2)
        self.root.mainloop()
#----------------------------------------------------------------------------------------------------------------
    def return_HomePage(self,event):

        self.win.withdraw()   # Hide window2
        self.root.deiconify() # Show window1
#----------------------------------------------------------------------------------------------------------------
    def show_Information(self,event,entry):

        global str_Search
        str_Search= StringVar()

        try:
            if entry:
            
                db=DAL()
                uniInfo=db.searchInfo(entry)
                if uniInfo != []:
            
                    self.win = Toplevel(self.root)
                    self.win.title("لیست دانشگاهها")
                    self.win.iconbitmap("UI/Icon/university.ico")
                    self.set_Form_Size(self.win,800,350)

                    table_Frame = Frame(self.win)
                    table_Frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

                    tree = ttk.Treeview(table_Frame, column=("title", "webSite"), show='headings', height=5)
                    tree.grid(row=1, columnspan=1)
                    tree.column("# 1", anchor=CENTER, width=300)
                    tree.heading("# 1", text="نام دانشگاه")
                    tree.column("# 2", anchor=CENTER, width=500)
                    tree.heading("# 2", text="آدرس اینترنتی")

                    i=0
                    for university in uniInfo:
                        tree.insert('', 'end', text=str(i), values=(university[0],university[1]))
                    i+=1 
                        
                    tree.pack(fill=BOTH, expand=True)

                    button_Frame=Frame(self.win)
                    button_Frame.pack(padx=10,pady=10)

                    return_Button = Button(button_Frame, text='بازگشت', bd=2, bg='#138D75')
                    return_Button.grid(columnspan=2)
                    return_Button.bind('<Button>',lambda event:self.return_HomePage(event))

                    self.win.mainloop()

                else:
                  
                    msg1 = Message(master=self.root, textvariable=str_Search, width=100,fg='red',justify='center')  
                    msg1.grid(row=6,column=1,columnspan=3) 
                    str_Search.set('اطلاعات یافت نشد')

            else:
                
                msg2 = Message(master=self.root, textvariable=str_Search, width=100,fg='red',justify='center')  
                msg2.grid(row=6,column=1,columnspan=3)
                str_Search.set(' فیلد خالی است ')

        except:
                msg3 = Message(master=self.root, textvariable=str_Search, width=100,fg='red',justify='center')  
                msg3.grid(row=6,column=1,columnspan=3)
                str_Search.set('خطا در برقراری ارتباط با پایگاه داده')

               

        
    


      


