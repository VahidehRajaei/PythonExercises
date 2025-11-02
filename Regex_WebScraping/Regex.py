import re

with open('information.txt','r') as file1:
    textFile=file1.read()

def write_Info(info):
    with open('information.csv','a') as file2:
        file2.write (f'\n{info}')


def search_Info():

    titleInfo='Name,Family,Mobile,Postal_Code,City'
    write_Info(titleInfo)

    listInfo=re.findall(r'Name:.+,Family:.+,Mobile:0912\d{7},Postal Code:\d{10},city:Tehran',textFile)
    for info in listInfo:
        personInfo=re.sub(r'Name:(.+),Family:(.+),Mobile:(0912\d{7}),Postal Code:(\d{10}),city:(Tehran)','\\g<1>,\\g<2>,\\g<3>,\\g<4>,\\g<5>',info)
        write_Info(personInfo)
    

search_Info()
