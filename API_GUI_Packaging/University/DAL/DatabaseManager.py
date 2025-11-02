from DAL.DbConnection import *
#------------------------------------------------------------------------------------------------------------
class DAL:

    def __init__(self):
        self.db=dbConnect()
        self.myCursor=self.db.cursor()
#------------------------------------------------------------------------------------------------------------
    def createTable(self,tableName):

        try:

            val=(str(tableName))
            query='''create table %s (
            universityid int auto_increment primary key,
            country varchar(50),
            universityname varchar(100),
            alpha_code varchar(2),
            state_province varchar(50),
            domains varchar(100),
            web_pages varchar(100)
            )''' % (val)
            self.myCursor.execute(query)
            self.db.commit()
            print('Table Successfully Created...')
            return True

        except:
            print('Exception In CreateTable...')
            return False
#------------------------------------------------------------------------------------------------------------
    def insertInfo(self,uniInfo):

        try:
            val=uniInfo.country,uniInfo.universityname,uniInfo.alpha_code,uniInfo.state_province,str(uniInfo.domains),str(uniInfo.web_pages)
            query='INSERT INTO tb_university(country,universityname,alpha_code,state_province,domains,web_pages)values(%s,%s,%s,%s,%s,%s)'
            self.myCursor.execute(query,val)
            self.db.commit()
            print('Data Successfully Insert...')
            return True
        
        except:
            print('Exception In Insert...')
            return False
#------------------------------------------------------------------------------------------------------------
    def searchInfo(self,state_province):

        try:
            
            val=[str(state_province)]
            query='SELECT universityname,web_pages FROM tb_university WHERE state_province=%s'
            self.myCursor.execute(query,val)
            searchResult=self.myCursor.fetchall()
            if searchResult is not None: 
                return searchResult
        
        except:
            print('Exception In Search...')
            return False
#------------------------------------------------------------------------------------------------------------        

        



