from DAL.BookModel import Book
from DAL.DbConnection import *
#------------------------------------------------------------------------------------------------------------
class DAL:

    def __init__(self):
        self.db=dbConnect()
        self.myCursor=self.db.cursor()
#------------------------------------------------------------------------------------------------------------
    
    def insertBook(self,book):

        try:
            val=book.bookcode,book.title,book.author,book.publisher
            query='INSERT INTO book(bookcode,title,author,publisher)values(%s,%s,%s,%s)'
            self.myCursor.execute(query,val)
            self.db.commit()
            return True
        
        except:
            print('Exception In Insert...')
            return False
#------------------------------------------------------------------------------------------------------------
        
    def deleteBook(self,bookcode):

        try:
            val=[int(bookcode)]
            query1='SELECT bookid FROM book WHERE bookcode=%s'
            self.myCursor.execute(query1,val)
            selectResult=self.myCursor.fetchone()
          
            if selectResult is not None: 
                query2='''
                    DELETE FROM book WHERE bookid =
                   (SELECT * FROM (SELECT bookid FROM book WHERE bookcode=%s) as b)'''
                self.myCursor.execute(query2,val)
                self.db.commit()
                return True
        
        except:
            print('Exception In Delete...')
            return False
#------------------------------------------------------------------------------------------------------------        

    def searchBook(self,bookcode):

        try:
            
            val=[int(bookcode)]
            query='SELECT * FROM book WHERE bookcode=%s'
            self.myCursor.execute(query,val)
            return self.myCursor.fetchone()
        
        except:
            print('Exception In Search...')
            return False
#------------------------------------------------------------------------------------------------------------        
    def showBooks(self):

        try:
            
            self.myCursor.execute('SELECT * FROM book')
            return self.myCursor.fetchall()
              
        except:
            print('Exception In Select...')
            return False
        
        



