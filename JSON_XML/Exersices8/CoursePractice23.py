import json
import jmespath

with open('employee.json','r') as file1:
    jsonStr=json.load(file1)

result1=jmespath.search('[?gender==`female`].fullName',jsonStr)
print(f'\nNames and family of female employees in all companies:\n\n{result1}')
print(150*'-')
result2=jmespath.search('[?gender==`male` && company==`MAPNA`].fullName',jsonStr)
print(f'Names and family of male employees of MAPNA company:\n\n{result2}')
print(150*'-')
result3=jmespath.search('[?company==`Iran Khodro Co.`].[fullName,email]',jsonStr)
print(f'Names and family and e-mails of employees of the company. Iran Khodro Co:\n\n{result3}')
print(150*'-')
#jmespath.search('max_by(@,&salary).*',jsonStr)
#فقط بیشترین عنصر را انتخاب می کرد از این رو لیست بصورت نزولی مرتب و سه عنصر اول انتخاب شد max چون تابع 
result4=jmespath.search('([?gender==`male`]|(sort_by(@,&salary)[::-1]))[0:3].*',jsonStr)
print(f'Full information of the first three men in terms of salary:\n\n{result4}\n')
