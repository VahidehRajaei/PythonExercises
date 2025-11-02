
class My_Exception_Handling(Exception):
    def __init__(self,message):
         super().__init__(message)
         self.message=message

    def __str__(self) :
        return f'Error is:\t{self.message}'
#------------------------------------------------------------------------------------------------------------
class Player_Selection:

    players_List=[]
    def __init__(self,personCode,age,weight,height):
        self.personCode=personCode
        self.age=age
        self.weight=weight
        self.height=height

    @staticmethod   
    def check_Integer(value,valueType):
        if value.isdigit():
            return value
        else:
            if not isinstance(value,int): 
                raise RuntimeError(f'{valueType} is not valid...')
            
    @staticmethod   
    def check_Float(weight):
        try:
            weight=float(weight)
        except:
            if not isinstance(weight,float): 
                raise RuntimeError('Weight is not valid...')
            
    def ageValidation(age):

        Player_Selection.check_Integer(age,'Age')
        age = int(age)
        if age<15 or 35<age:
            raise My_Exception_Handling('Age out of range\nThis person is not allowed to register')
        return age
    
    def age_WeightValidation(age,weight):

        Player_Selection.check_Float(weight)
        weight=float(weight)

        if age>15 and 25>age:
            if weight>80 or 60>weight:
                raise My_Exception_Handling('Weight out of range\nThis person is not allowed to register')
        elif age>25 and 35>age:
            if weight>75 or 50>weight:
                raise My_Exception_Handling('Weight out of range\nThis person is not allowed to register')
            
        return age,weight
    
    def heightvalidation(height):

        Player_Selection.check_Integer(height,'Height')
        height = int(height)

        if height<170 or height>190:
            raise My_Exception_Handling('Height out of range\nThis person is not allowed to register')
        
        return height

    def register_Player(personCode,age,weight,height):

        try:
                    age=Player_Selection.ageValidation(age)
                    age,weight=Player_Selection.age_WeightValidation(age,weight)
                    height=Player_Selection.heightvalidation(height)
                    Player_Selection.players_List.append((personCode,age,weight,height))
                    
        except My_Exception_Handling as error:
            print(error) 

        except RuntimeError as error:
            print(error)

#------------------------------------------------------------------------------------------------------------
while True:
        
        personCode = int(input('Enter the player code (0 to Exit):'))
        if personCode == 0:
            print("Program terminated.")
            break
        age = input('Enter the player age:')
        weight =input('Enter the player weight:')
        height = input('Enter the player height:')

        Player_Selection.register_Player(personCode, age, weight, height)

print('Following registrations is successfully completed:')
print(Player_Selection.players_List)




