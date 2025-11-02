class Food_Menu:

    def __init__(self,foodCode,foodName,foodPrice,*food_Materials):
        self.foodCode=foodCode
        self.foodName=foodName
        self.foodPrice=foodPrice
        self.food_Materials=self.addMaterials(*food_Materials)

    def addMaterials(self,*args):
        material_List=[]
        for item in args:
            material_List.append(item)
        return material_List
    
    # def __str__(self):
    #     return f'{self.foodCode}\t\t{self.foodName}\t{self.foodPrice}\t\t{self.food_Materials}'

#------------------------------------------------------------------------------------------------------
import json

def createFoodMenu(foodCode,foodName,foodPrice,*food_Materials):

    menuSample=Food_Menu(foodCode,foodName,foodPrice,*food_Materials)
    return menuSample.__dict__
#-----------------------------------------Create&ReadFromJSON-------------------------------------------
import os

def Food_MenuJsonFile():

    if not os.path.exists('foodMenu.json'):

        with open("foodMenu.json",'x') as file1:
            
            try:
                currentFoodMenu=json.load(file1)

            except:
                currentFoodMenu=[]
    else:
    
        with open("foodMenu.json",'w') as file1: 

            try:
                currentFoodMenu=json.load(file1)

            except:
                currentFoodMenu=[]

    return currentFoodMenu
#------------------------------------------WriteToJSON--------------------------------------------------
def writeFood_MenuToJsonFile(foodMenu):
        
        with open("foodMenu.json",'w') as file1:
            json.dump(foodMenu,file1,indent=4)
#-------------------------------------------Sample------------------------------------------------------
currentFoodMenu=Food_MenuJsonFile() 

menu1=createFoodMenu(101,'Khoresht GhormeSabzi',1500000,'Redmeat','Redbeans','Vegetable','Lemon') 
currentFoodMenu.append(menu1)
menu2=createFoodMenu(102,'Khoresht Karafs',1400000,'RedMeat','Celery','Vegetable','Lemon')                            
currentFoodMenu.append(menu2)
menu3=createFoodMenu(103,'Khoresht Gheyme',1300000,'RedMeat','Cotyledon','Potato','Lemon')  
currentFoodMenu.append(menu3)
menu4=createFoodMenu(104,'Zeresk Polo',2400000,'Rice','Chicken','Barberry')                            
currentFoodMenu.append(menu4)
menu5=createFoodMenu(105,'Sabzi Polo',2800000,'Rice','Fish','Vegetable')                            
currentFoodMenu.append(menu5)
menu6=createFoodMenu(106,'Joje Kabab',3000000,'Rice','Chiken','Tomato')                            
currentFoodMenu.append(menu6)
menu7=createFoodMenu(107,'Barg Kabab',5800000,'Rice','Redmeat','Tomato')                            
currentFoodMenu.append(menu7)
menu8=createFoodMenu(108,'Lobiya Polo',2000000,'Rice','RedMeat','Greenbeans')                            
currentFoodMenu.append(menu8)
menu9=createFoodMenu(109,'Pizza',1800000,'Mushroom','Chickenham','Olive','Cheese')                            
currentFoodMenu.append(menu9)
menu10=createFoodMenu(110,'Salad Sezar',2450000,'Chicken','Toastbread','Vegetable','ParmesanCheese')                            
currentFoodMenu.append(menu10)

writeFood_MenuToJsonFile(currentFoodMenu)   

