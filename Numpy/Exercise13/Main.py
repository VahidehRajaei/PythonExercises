import numpy as np
from numpy import unravel_index

#-------------------------------------------------------
def readFile(fileName,fileMode):
    
    with open (fileName,fileMode) as f:
        rowList = []
        for line in  f.readlines():
            rowList.append(line.replace("\n", ""))
            newArry=np.array(rowList)
            newArry=newArry.astype('float64')
        matrix=newArry.reshape(3,5)
        return matrix
#--------------------------------------------------------
def rainAverage(matrix):
    monthList=[]
    for row in matrix:
        monthList.append(np.average(row)) 
    monthArray=np.array(monthList)
    return monthArray
#======================================Show matrix of files=============================================

Matrix_2019=readFile('precipitation_fall_2019.txt','r')
print(f'\n**** Matrix of rain fall_2019 ****\n\n{Matrix_2019}')
print(35*'-')
Matrix_2020=readFile('precipitation_fall_2020.txt','r')
print(f'\n**** Matrix of rain fall_2020 ****\n\n{Matrix_2020}')
print(35*'-')
Matrix_2021=readFile('precipitation_fall_2021.txt','r')
print(f'\n**** Matrix of rain fall_2021 ****\n\n{Matrix_2021}')
print(70*'-')

#=====================================Show average of rainfall==========================================

arr2019=rainAverage(Matrix_2019)
print(f'Average precipitation in fall months of 2019 year :{arr2019}')
print(70*'-')
arr2020=rainAverage(Matrix_2020)
print(f'Average precipitation in fall months of 2020 year :{arr2020}')
print(70*'-')
arr2021=rainAverage(Matrix_2021)
print(f'Average precipitation in fall months of 2021 year :{arr2021}')
print(70*'-')

#=====================================Matrix of whole rainfall==========================================

totalArray=np.concatenate((arr2019,arr2020,arr2021))
totalMatrix=totalArray.reshape(3,3)
print(f'*** Total Matrix ***\n\n{totalMatrix}')
print(40*'-')

#========================================Maximum_Rainfall==================================================

maxRain=totalMatrix.max()
print(f'Max number in matrix: {np.round(maxRain,2)}\n')
dimension_Max=unravel_index(totalMatrix.argmax(),totalMatrix.shape)
print(f'Dimension of max number : {dimension_Max}\n') 

# سال 2021 و ماه آذر با مقدار بارش 46.38 (موقعیت 2*2 از ماتریس) بیشترین میزان بارندگی را داشته است