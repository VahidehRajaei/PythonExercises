def mainFun(func):
    def arrange(list1):
        newList=[]
        for item in list1:
            if type(item)==int and item>=0:
                newList.append(item)
        func(newList) 
    return arrange
   
@mainFun
def fact(list1): 
    tempList=[]
    for n in list1:
        j=1
        for i in range (1,n+1):
            j*=i
        tempList.append(j)
    print(tempList) 

#-----------------------------------Sample-------------------------------------
number_List = [4, 3, 8, 0, -3, -45, 2, 10, -16, 23, 9, 1, -6, 55, 3.4, 6, 11.5]
fact(number_List)

