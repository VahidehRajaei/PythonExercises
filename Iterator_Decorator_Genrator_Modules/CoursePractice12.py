from datetime import date
from khayyam import JalaliDate

def Date_conversion():

    dateInput=input("Enter Date (For Example: 1399-06-20):")
    dateJalali=JalaliDate.strptime(dateInput,'%Y-%m-%d')
    dateMiladi=dateJalali.todate()
    yield f'Result Of Converted Date: {dateMiladi}'
    dateToday=date.today()
    daydiff=abs(dateMiladi-dateToday).total_seconds()/(24*60*60)
    yield f'Result Of Difference Date: {int(daydiff)} Days'

#-----------------------------------Sample----------------------------------------
obj1=Date_conversion()
for item in obj1:
    print(item)




   
   
