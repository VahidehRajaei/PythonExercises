import collections

class MyString(collections.UserString):
   
    def insert (self, insert_Str, pos):
        self.data=self.data[:pos] + insert_Str + self.data[pos:]

    def reverse(self):
        self.data=self.data[::-1]

#------------------------------Sample------------------------------------

str1=MyString('Vahideh pour')
str1.insert('Rajaei',8) #Insert the desired string into the desired position
print(f'\nThe Result of Insert String:\t{str1}')


str1=MyString('python')
str1.reverse() 
print(f'The Result Of Reverse String:\t{str1}\n')


