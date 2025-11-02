import sys
sys.path.insert(0,'D:/PythonClass/Library')
#------------------------------------------------------------------------------------------------------------

class Book:

    def __init__(self,bookcode,title,author,publisher):
        self.bookcode=bookcode
        self.title=title
        self.author=author
        self.publisher=publisher
        