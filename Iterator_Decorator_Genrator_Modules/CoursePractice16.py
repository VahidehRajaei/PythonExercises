import collections

student_List1 = [{"Name":"Ali Rezaee", "Age":25},{"Name":"RezaAhmadi","Age":28},{"Name":"Sara Akbari","Age":25},
                 {"Name":"BaharNajafi","Age":23},{"Name":"Iman Mohamadi","Age":25},{"Name":"SimaShaker","Age":25},
                 {"Name":"Negin Ghazi","Age":29},{"Name":"MaryamYaghoubi","Age":25},{"Name":"Mitra Sharif","Age":23},
                 {"Name":"Ahmad Moradi","Age":25}]

student_List2 = [{"Name":"Amir Radi", "Age":23},{"Name":"RezaArdakani","Age":23},{"Name":"Sima Sadr","Age":26},
                {"Name":"BahmanNajafi","Age":30},{"Name":"Mina Mohamadi","Age":23},{"Name":"MitraMoradi","Age":23},
                {"Name":"Narges Arab","Age":30},{"Name":"Ali Eshtiyaghi","Age":32}]


def countAge(list1):
    temp=[]
    for dic1 in list1:
        for k,v in dic1.items():
            if k=='Age':
                temp.append(v)
    return collections.Counter(temp).most_common(1)

#------------------------------------------------Sample-------------------------------------------------------------------
print(f'\nOutput\n'+20*'-')
result1=countAge(student_List1)
for item in result1:
    print(f'Group1:{item}')

result2=countAge(student_List2)
for item in result2:
    print(f'Group2:{item}\n')

