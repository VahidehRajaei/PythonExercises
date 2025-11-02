from mysql.connector import connect,Error
#------------------------------------------------------------------------------------------------------------
def dbConnect():

    try:
        return connect(host='localhost',user='root',password='123456',database='db_university')
    
    except Error as error:
        print(error)