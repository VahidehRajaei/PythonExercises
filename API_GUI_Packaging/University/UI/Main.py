import sys
sys.path.insert(0,'D:/PythonClass/University')

from UI.UniversityGui import *
from PL.ScrapAPI import *

#=======================================Create_Table=============================================
db=DAL()
db.createTable(tableName='tb_university')
#=======================================Insert_Table=============================================
db=DAL()
dbRows=get_University_Info()
for dbRow in dbRows:
    db.insertInfo(dbRow)
#=====================================Form_Running=============================================
university_Search_Form = Gui()




